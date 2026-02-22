import streamlit as st
import pandas as pd
import os
import datetime
from pulp import *

st.set_page_config(page_title="Ferro Alloy Optimizer", layout="wide")

st.title("Ferro Alloy Optimization Model")

# =========================
# LOAD EXCEL FILE
# =========================

file_path = "grade.xlsx"

uploaded = st.file_uploader("Upload Grade File (Optional)", type=["xlsx"])

if uploaded is not None:
    df = pd.read_excel(uploaded)
elif os.path.exists(file_path):
    df = pd.read_excel(file_path)
else:
    st.error("No Excel file found")
    st.stop()

st.subheader("Raw Data")
st.dataframe(df)

# =========================
# USER INPUTS
# =========================

st.sidebar.header("Blow End Chemistry")

elements = ["C", "Mn", "Si", "P", "S"]

blow = {}
min_lim = {}
max_lim = {}

for e in elements:
    blow[e] = st.sidebar.number_input(f"Blow End {e}", value=0.0)
    min_lim[e] = st.sidebar.number_input(f"Min {e}", value=0.0)
    max_lim[e] = st.sidebar.number_input(f"Max {e}", value=0.0)

st.sidebar.header("Bunker Availability")

bunker = {}
for mat in df["Material"]:
    bunker[mat] = st.sidebar.selectbox(
        f"{mat}", [1, 0], index=0
    )

# =========================
# SOLVE BUTTON
# =========================

if st.button("Run Optimization"):

    prob = LpProblem("FerroOptimization", LpMinimize)

    # VARIABLES
    qty = {
        row["Material"]: LpVariable(row["Material"], lowBound=0)
        for _, row in df.iterrows()
    }

    # OBJECTIVE
    prob += lpSum(qty[m] * df.loc[df.Material == m, "Cost"].values[0] for m in qty)

    # =========================
    # CONSTRAINTS
    # =========================

    for e in elements:

        prob += (
            lpSum(
                qty[m] * df.loc[df.Material == m, e].values[0]
                for m in qty
            )
            + blow[e]
            >= min_lim[e]
        )

        prob += (
            lpSum(
                qty[m] * df.loc[df.Material == m, e].values[0]
                for m in qty
            )
            + blow[e]
            <= max_lim[e]
        )

    # =========================
    # BUNKER AVAILABILITY
    # =========================

    for m in qty:
        if bunker[m] == 0:
            prob += qty[m] == 0

    # =========================
    # SOLVE
    # =========================

    prob.solve()

    st.subheader("Status")
    st.write(LpStatus[prob.status])

    if prob.status != 1:
        st.error("No feasible solution")
        st.stop()

    # =========================
    # RESULTS
    # =========================

    results = []

    for v in prob.variables():
        if v.varValue > 0:
            results.append([v.name, round(v.varValue, 2)])

    result_df = pd.DataFrame(results, columns=["Material", "Qty"])

    st.subheader("Required Additions")
    st.dataframe(result_df)

    cost = round(value(prob.objective), 2)

    st.success(f"Minimum Cost = {cost}")

    # =========================
    # SAVE LOG
    # =========================

    def save_log(data):
        file = "run_log.csv"
        df_log = pd.DataFrame([data])
        if not os.path.isfile(file):
            df_log.to_csv(file, index=False)
        else:
            df_log.to_csv(file, mode="a", header=False, index=False)

    log_data = {
        "Time": datetime.datetime.now(),
        "Cost": cost,
        "Status": LpStatus[prob.status]
    }

    save_log(log_data)

    st.info("Run saved to log file")