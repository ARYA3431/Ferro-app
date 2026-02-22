from pulp import *
import pandas as pd
import streamlit as st

st.title("Ferroalloy Model with Optimal Cost")

# =========================
# LOAD FILES
# =========================
cost_df = pd.read_excel("details.xlsx", sheet_name="cost", index_col=0)
FA_df = pd.read_excel("details.xlsx", sheet_name="FA_details")
FA_df.set_index("Ferroalloy", inplace=True)

# =========================
# LOAD GRADE FILE
# =========================
df = pd.read_excel("grade.xlsx")
df["Dolvi grades"] = df["Dolvi grades"].str.upper()

grade = st.selectbox("Select Grade", df["Dolvi grades"].unique())
filtered_df = df[df["Dolvi grades"] == grade]

# Fix infeasible Si aim
if filtered_df["si_aim"].iloc[0] == 0:
    filtered_df.loc[filtered_df.index[0], "si_aim"] = 0.009

# =========================
# DISPLAY TARGET TABLE
# =========================
min_max_df = pd.DataFrame({
    "Elements": ["Min", "Max", "Aim"],
    "C": [filtered_df["c_min"].iloc[0], filtered_df["c_max"].iloc[0], filtered_df["c_aim"].iloc[0]],
    "Mn": [filtered_df["mn_min"].iloc[0], filtered_df["mn_max"].iloc[0], filtered_df["mn_aim"].iloc[0]],
    "S": [filtered_df["s_min"].iloc[0], filtered_df["s_max"].iloc[0], filtered_df["s_aim"].iloc[0]],
    "P": [filtered_df["p_min"].iloc[0], filtered_df["p_max"].iloc[0], filtered_df["p_aim"].iloc[0]],
    "Si": [filtered_df["si_min"].iloc[0], filtered_df["si_max"].iloc[0], filtered_df["si_aim"].iloc[0]]
})

st.write(min_max_df)

# =========================
# INPUT CHEMISTRY
# =========================
st.subheader("Enter Blow End Chemistry")

col1, col2, col3 = st.columns(3)
Carbon = col1.number_input("C", format="%.3f")
Manganese = col2.number_input("Mn", format="%.3f")
Sulphur = col3.number_input("S", format="%.3f")

col4, col5, col6 = st.columns(3)
Phosphorus = col4.number_input("P", format="%.3f")
Silicon = col5.number_input("Si", format="%.3f")
Tap_Weight = col6.number_input("Tap Weight", value=350)

# =========================
# SIDEBAR INPUTS
# =========================
with st.sidebar:

    st.subheader("Bunker Availability")

    col1, col2 = st.columns(2)

    col1.write("Recovery")

    SiMn1 = col1.number_input("SiMn", 0.0,1.0,1.0)
    HCMn1 = col1.number_input("HCMn",0.0,1.0,1.0)
    MCMn1 = col1.number_input("MCMn",0.0,1.0,1.0)
    LCMn1 = col1.number_input("LCMn",0.0,1.0,1.0)
    MtMn1 = col1.number_input("MtMn",0.0,1.0,1.0)
    FeSi1 = col1.number_input("FeSi",0.0,1.0,1.0)
    CPC1  = col1.number_input("CPC",0.0,1.0,1.0)

    col2.write("Limit")

    SiMn_limit = col2.number_input("SiMn limit", value=9999)
    HCMn_limit = col2.number_input("HCMn limit", value=9999)
    MCMn_limit = col2.number_input("MCMn limit", value=9999)
    LCMn_limit = col2.number_input("LCMn limit", value=9999)
    MtMn_limit = col2.number_input("MtMn limit", value=9999)
    FeSi_limit = col2.number_input("FeSi limit", value=9999)
    CPC_limit  = col2.number_input("CPC limit", value=9999)

# =========================
# MODEL FUNCTION
# =========================
def model():

    prob = LpProblem("Min Cost", LpMinimize)

    # Variables
    SiMn = LpVariable("SiMn",0,SiMn_limit)
    HCMn = LpVariable("HCMn",0,HCMn_limit)
    MCMn = LpVariable("MCMn",0,MCMn_limit)
    LCMn = LpVariable("LCMn",0,LCMn_limit)
    MtMn = LpVariable("MtMn",0,MtMn_limit)
    FeSi = LpVariable("FeSi",0,FeSi_limit)
    CPC  = LpVariable("CPC",0,CPC_limit)

    # Objective
    prob += (
        cost_df.loc["SiMn","COST"]*SiMn +
        cost_df.loc["HCMn","COST"]*HCMn +
        cost_df.loc["MCMn","COST"]*MCMn +
        cost_df.loc["LCMn","COST"]*LCMn +
        cost_df.loc["FeSi","COST"]*FeSi +
        cost_df.loc["MtMn","COST"]*MtMn +
        cost_df.loc["CPC","COST"]*CPC
    )

    # =================
    # Constraints
    # =================

    # Carbon
    prob += (
        FA_df.loc["SiMn","C"]*SiMn1*SiMn +
        FA_df.loc["HCMn","C"]*HCMn1*HCMn +
        FA_df.loc["MCMn","C"]*MCMn1*MCMn +
        FA_df.loc["LCMn","C"]*LCMn1*LCMn +
        FA_df.loc["FeSi","C"]*FeSi1*FeSi +
        FA_df.loc["MtMn","C"]*MtMn1*MtMn +
        FA_df.loc["CPC","C"]*CPC1*CPC
        ==
        (filtered_df["c_aim"].iloc[0] - Carbon)*Tap_Weight*10
    )

    # Silicon
    prob += (
        FA_df.loc["SiMn","Si"]*SiMn1*SiMn +
        FA_df.loc["HCMn","Si"]*HCMn1*HCMn +
        FA_df.loc["MCMn","Si"]*MCMn1*MCMn +
        FA_df.loc["LCMn","Si"]*LCMn1*LCMn +
        FA_df.loc["FeSi","Si"]*FeSi1*FeSi +
        FA_df.loc["MtMn","Si"]*MtMn1*MtMn +
        FA_df.loc["CPC","Si"]*CPC1*CPC
        ==
        (filtered_df["si_aim"].iloc[0] - Silicon)*Tap_Weight*10
    )

    # Manganese
    prob += (
        FA_df.loc["SiMn","Mn"]*SiMn1*SiMn +
        FA_df.loc["HCMn","Mn"]*HCMn1*HCMn +
        FA_df.loc["MCMn","Mn"]*MCMn1*MCMn +
        FA_df.loc["LCMn","Mn"]*LCMn1*LCMn +
        FA_df.loc["FeSi","Mn"]*FeSi1*FeSi +
        FA_df.loc["MtMn","Mn"]*MtMn1*MtMn +
        FA_df.loc["CPC","Mn"]*CPC1*CPC
        ==
        (filtered_df["mn_aim"].iloc[0] - Manganese)*Tap_Weight*10
    )

    # Phosphorus
    prob += (
        FA_df.loc["SiMn","P"]*SiMn1*SiMn +
        FA_df.loc["HCMn","P"]*HCMn1*HCMn +
        FA_df.loc["MCMn","P"]*MCMn1*MCMn +
        FA_df.loc["LCMn","P"]*LCMn1*LCMn +
        FA_df.loc["FeSi","P"]*FeSi1*FeSi +
        FA_df.loc["MtMn","P"]*MtMn1*MtMn +
        FA_df.loc["CPC","P"]*CPC1*CPC
        <=
        (filtered_df["p_aim"].iloc[0] - Phosphorus)*Tap_Weight*10
    )

    # Sulphur
    prob += (
        FA_df.loc["SiMn","S"]*SiMn1*SiMn +
        FA_df.loc["HCMn","S"]*HCMn1*HCMn +
        FA_df.loc["MCMn","S"]*MCMn1*MCMn +
        FA_df.loc["LCMn","S"]*LCMn1*LCMn +
        FA_df.loc["FeSi","S"]*FeSi1*FeSi +
        FA_df.loc["MtMn","S"]*MtMn1*MtMn +
        FA_df.loc["CPC","S"]*CPC1*CPC
        <=
        (filtered_df["s_aim"].iloc[0] - Sulphur)*Tap_Weight*10
    )

    # Solve
    prob.solve()

    # Results
    st.subheader("Results")

    st.write("Status:", LpStatus[prob.status])
    st.write("Minimum Cost =", round(value(prob.objective),0))

    st.write("SiMn =", value(SiMn))
    st.write("HCMn =", value(HCMn))
    st.write("MCMn =", value(MCMn))
    st.write("LCMn =", value(LCMn))
    st.write("FeSi =", value(FeSi))
    st.write("MtMn =", value(MtMn))
    st.write("CPC =", value(CPC))

# =========================
# RUN BUTTON
# =========================
if st.button("Predict"):
    model()