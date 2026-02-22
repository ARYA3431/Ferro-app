from pulp import *
import pandas as pd
import streamlit as st
from pulp import LpProblem, value
from pulp import LpStatus, LpStatusInfeasible
# all the conditions which causes infeasible result
if filtered_df['si_aim'].iloc[0] == 0:
    # fix simn zero
    filtered_df.loc[filtered_df.index[0], 'si_aim'] = 0.009
else:
    filtered_df.loc[filtered_df.index[0], 'si_aim'] = filtered_df['si_aim'].iloc[0]


min_max_df = pd.DataFrame({
    'Elements': ['Min', 'Max', 'Aim'],
    'C': [filtered_df['c_min'].iloc[0], filtered_df['c_max'].iloc[0], filtered_df['c_aim'].iloc[0]],
    'Mn': [filtered_df['mn_min'].iloc[0], filtered_df['mn_max'].iloc[0], filtered_df['mn_aim'].iloc[0]],
    'S': [filtered_df['s_min'].iloc[0], filtered_df['s_max'].iloc[0], filtered_df['s_aim'].iloc[0]],
    'P': [filtered_df['p_min'].iloc[0], filtered_df['p_max'].iloc[0], filtered_df['p_aim'].iloc[0]],
    'Si': [filtered_df['si_min'].iloc[0], filtered_df['si_max'].iloc[0], filtered_df['si_aim'].iloc[0]],
    'Al': [filtered_df['al_min'].iloc[0], filtered_df['al_max'].iloc[0], filtered_df['al_aim'].iloc[0]],
    'Cr': [filtered_df['cr_min'].iloc[0], filtered_df['cr_max'].iloc[0], filtered_df['cr_aim'].iloc[0]],
    'Cu': [filtered_df['cu_min'].iloc[0], filtered_df['cu_max'].iloc[0], filtered_df['cu_aim'].iloc[0]],
    'V': [filtered_df['v_min'].iloc[0], filtered_df['v_max'].iloc[0], filtered_df['v_aim'].iloc[0]],
    'Ti': [filtered_df['ti_min'].iloc[0], filtered_df['ti_max'].iloc[0], filtered_df['ti_aim'].iloc[0]],
    'Nb': [filtered_df['nb_min'].iloc[0], filtered_df['nb_max'].iloc[0], filtered_df['nb_aim'].iloc[0]],
    'Mo': [filtered_df['mo_min'].iloc[0], filtered_df['mo_max'].iloc[0], filtered_df['mo_aim'].iloc[0]],
    'B': [filtered_df['b_min'].iloc[0], filtered_df['b_max'].iloc[0], filtered_df['b_aim'].iloc[0]],
    'Ca': [filtered_df['ca_min'].iloc[0], filtered_df['ca_max'].iloc[0], filtered_df['ca_aim'].iloc[0]]
})

st.write(min_max_df[['Elements', 'C', 'Mn', 'S', 'P', 'Si', 'Al', 'Cr', 'Cu', 'V', 'Ti', 'Nb', 'Mo', 'B', 'Ca']])

st.markdown("<h2 style='text-align: left; color: white; font-size: 15px;'>Enter the blow end chemistry</h2>", unsafe_allow_html=True)

container = st.container()

col1, col2, col3 = container.columns(3)

Carbon = col1.number_input("C", format="%.3f")
Manganese = col2.number_input("Mn", format="%.3f")
Sulphur = col3.number_input("S", format="%.3f")

col4, col5, col6 = container.columns(3)

Phosphorus = col4.number_input("P", format="%.3f")
Silicon = col5.number_input("Si", format="%.3f")
Tap_Weight = col6.number_input("Tap_Weight", value=350)


if Carbon >= filtered_df['c_aim'].iloc[0]:
    filtered_df.loc[filtered_df.index[0], 'c_aim'] = filtered_df['c_max'].iloc[0]
    filtered_df.loc[filtered_df.index[0], 'c_max'] = filtered_df['c_aim'].iloc[0]


# sidebar function
with st.sidebar:
    st.subheader("Availibility of bunkers:")

    col1, col2 = st.columns(2)

    col1.write("Materials")
    SiMn1 = col1.number_input("SiMn1", min_value=0.0, max_value=1.0, value=1.0, step=1.0)
    HCMn1 = col1.number_input("HCMn1", min_value=0.0, max_value=1.0, value=1.0, step=1.0)
    MCMn1 = col1.number_input("MCMn1", min_value=0.0, max_value=1.0, value=1.0, step=1.0)
    LCMn1 = col1.number_input("LCMn1", min_value=0.0, max_value=1.0, value=1.0, step=1.0)
    MtMn1 = col1.number_input("MtMn1", min_value=0.0, max_value=1.0, value=1.0, step=1.0)
    FeSi1 = col1.number_input("FeSi1", min_value=0.0, max_value=1.0, value=1.0, step=1.0)
    CPC1 = col1.number_input("CPC1", min_value=0.0, max_value=1.0, value=1.0, step=1.0)

    col2.write("Limit")
    SiMn_limit = col2.number_input("SiMn_Limit", value=9999)
    HCMn_limit = col2.number_input("HCMn_Limit", value=9999)
    MCMn_limit = col2.number_input("MCMn_Limit", value=9999)
    LCMn_limit = col2.number_input("LCMn_Limit", value=9999)
    MtMn_limit = col2.number_input("MtMn_Limit", value=9999)
    FeSi_limit = col2.number_input("FeSi_Limit", value=9999)
    CPC_limit = col2.number_input("CPC_Limit", value=9999)

    if SiMn1 == 0:
        SiMn_limit = 0
    if HCMn1 == 0:
        HCMn_limit = 0
    if MCMn1 == 0:
        MCMn_limit = 0
    if LCMn1 == 0:
        LCMn_limit = 0
    if MtMn1 == 0:
        MtMn_limit = 0
    if CPC1 == 0:
        CPC_limit = 0


if st.button("Predict"):
    model()