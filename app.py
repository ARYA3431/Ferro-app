from pulp import *
import pandas as pd
import streamlit as st
from pulp import LpStatus, LpStatusInfeasible, value

st.title('Ferroalloy Model with Optimal Cost')


def model():

    cost_df = pd.read_excel('details.xlsx', sheet_name='cost', index_col=0)
    FA_df = pd.read_excel('details.xlsx', sheet_name='FA_details')
    FA_df.set_index('Ferroalloy', inplace=True)

    prob1 = LpProblem("LP Problem", LpMinimize)
    prob2 = LpProblem("LP Problem", LpMaximize)

    # VARIABLES
    SiMn = LpVariable("SiMn", 0, SiMn_limit)
    HCMn = LpVariable("HCMn", 0, HCMn_limit)
    MCMn = LpVariable("MCMn", 0, MCMn_limit)
    LCMn = LpVariable("LCMn", 0, LCMn_limit)
    MtMn = LpVariable("MtMn", 0, MtMn_limit)
    FeSi = LpVariable("FeSi", 0, FeSi_limit)
    CPC = LpVariable("CPC", 0, CPC_limit)

    # OBJECTIVE MIN COST
    prob1 += (
        cost_df.loc["SiMn","COST"]*SiMn +
        cost_df.loc["HCMn","COST"]*HCMn +
        cost_df.loc["MCMn","COST"]*MCMn +
        cost_df.loc["LCMn","COST"]*LCMn +
        cost_df.loc["FeSi","COST"]*FeSi +
        cost_df.loc["MtMn","COST"]*MtMn +
        cost_df.loc["CPC","COST"]*CPC
    )

    # CONSTRAINTS
    prob1 += (
        FA_df.loc['SiMn','C']*SiMn1*SiMn +
        FA_df.loc['HCMn','C']*HCMn1*HCMn +
        FA_df.loc['MCMn','C']*MCMn1*MCMn +
        FA_df.loc['LCMn','C']*LCMn1*LCMn +
        FA_df.loc['FeSi','C']*FeSi1*FeSi +
        FA_df.loc['MtMn','C']*MtMn1*MtMn +
        FA_df.loc['CPC','C']*CPC1*CPC
        == (filtered_df['c_aim'].iloc[0] - Carbon) * Tap_Weight * 10
    )

    prob1.solve()

    st.write("Status:", LpStatus[prob1.status])
    st.write("Minimum cost =", round(value(prob1.objective),0))

    st.write("SiMn =", value(SiMn), "kg")
    st.write("HCMn =", value(HCMn), "kg")
    st.write("MCMn =", value(MCMn), "kg")
    st.write("LCMn =", value(LCMn), "kg")
    st.write("FeSi =", value(FeSi), "kg")
    st.write("CPC =", value(CPC), "kg")
    st.write("MtMn =", value(MtMn), "kg")


# ---------------- GRADE INPUT ----------------

df = pd.read_excel("grade.xlsx")
df['Dolvi grades'] = df['Dolvi grades'].str.upper()

grade = st.selectbox('Select Grade', df['Dolvi grades'].unique())
filtered_df = df[df['Dolvi grades']==grade]


# FIX ZERO AIM CASE
if filtered_df['si_aim'].iloc[0] == 0:
    filtered_df.loc[filtered_df.index[0],'si_aim'] = 0.009


# DISPLAY LIMIT TABLE
min_max_df = pd.DataFrame({
    'Elements':['Min','Max','Aim'],
    'C':[filtered_df['c_min'].iloc[0],filtered_df['c_max'].iloc[0],filtered_df['c_aim'].iloc[0]],
    'Mn':[filtered_df['mn_min'].iloc[0],filtered_df['mn_max'].iloc[0],filtered_df['mn_aim'].iloc[0]],
    'S':[filtered_df['s_min'].iloc[0],filtered_df['s_max'].iloc[0],filtered_df['s_aim'].iloc[0]],
    'P':[filtered_df['p_min'].iloc[0],filtered_df['p_max'].iloc[0],filtered_df['p_aim'].iloc[0]],
    'Si':[filtered_df['si_min'].iloc[0],filtered_df['si_max'].iloc[0],filtered_df['si_aim'].iloc[0]]
})

st.write(min_max_df)


# ---------------- USER INPUT ----------------

col1,col2,col3 = st.columns(3)

Carbon = col1.number_input("C", format="%.3f")
Manganese = col2.number_input("Mn", format="%.3f")
Sulphur = col3.number_input("S", format="%.3f")

col4,col5,col6 = st.columns(3)

Phosphorus = col4.number_input("P", format="%.3f")
Silicon = col5.number_input("Si", format="%.3f")
Tap_Weight = col6.number_input("Tap Weight", value=350)


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.subheader("Availability of bunkers")

    SiMn1 = st.number_input("SiMn Recovery",0.0,1.0,1.0)
    HCMn1 = st.number_input("HCMn Recovery",0.0,1.0,1.0)
    MCMn1 = st.number_input("MCMn Recovery",0.0,1.0,1.0)
    LCMn1 = st.number_input("LCMn Recovery",0.0,1.0,1.0)
    MtMn1 = st.number_input("MtMn Recovery",0.0,1.0,1.0)
    FeSi1 = st.number_input("FeSi Recovery",0.0,1.0,1.0)
    CPC1 = st.number_input("CPC Recovery",0.0,1.0,1.0)

    SiMn_limit = st.number_input("SiMn Limit",0,9999,9999)
    HCMn_limit = st.number_input("HCMn Limit",0,9999,9999)
    MCMn_limit = st.number_input("MCMn Limit",0,9999,9999)
    LCMn_limit = st.number_input("LCMn Limit",0,9999,9999)
    MtMn_limit = st.number_input("MtMn Limit",0,9999,9999)
    FeSi_limit = st.number_input("FeSi Limit",0,9999,9999)
    CPC_limit = st.number_input("CPC Limit",0,9999,9999)


# ---------------- BUTTON ----------------

if st.button("Predict"):
    model()