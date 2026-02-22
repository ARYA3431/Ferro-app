from pulp import *
import pandas as pd
import streamlit as st
from pulp import LpStatus, LpStatusInfeasible

st.title('Ferroalloy Model with Optimal Cost')# :copyright:')
#st.title(':blue[Ferroalloy Model with Optimal Cost]:copyright:')
#st.subheader('Enter the target chemistry')
#st.markdown("<h2 style='text-align: left; color: white; font-size: 18px;'>Enter the target chemistry</h2>", unsafe_allow_html=True)
# st.subheader(':blue[Enter the target chemistry]')

def model():

    #taking cost details from sheet as Dataframe
    cost_df = pd.read_excel('details.xlsx', sheet_name='cost', index_col=0)

    #taking Ferro alloy details from sheet as Dataframe
    FA_df = pd.read_excel('details.xlsx', sheet_name='FA_details')

    # set the 'Ferroalloy' column as the index
    FA_df.set_index('Ferroalloy', inplace=True)

    # Define the problem
    prob1 = LpProblem("LP Problem", LpMinimize)
    prob2 = LpProblem("LP Problem", LpMaximize)

    # Create the variables with the user-defined upper bounds
    SiMn = LpVariable("SiMn", lowBound=0, upBound=SiMn_limit)
    HCMn = LpVariable("HCMn", lowBound=0, upBound=HCMn_limit)
    MCMn = LpVariable("MCMn", lowBound=0, upBound=MCMn_limit)
    LCMn = LpVariable("LCMn", lowBound=0, upBound=LCMn_limit)
    MtMn = LpVariable("MtMn", lowBound=0, upBound=MtMn_limit)
    FeSi = LpVariable("FeSi", lowBound=0, upBound=FeSi_limit)
    CPC = LpVariable("CPC", lowBound=0, upBound=CPC_limit)
    ELCSiMn = LpVariable("ELCSiMn", lowBound=0, upBound=ELCSiMn_limit)
    GP = LpVariable("GP", lowBound=0, upBound=GP_limit)
    FeV = LpVariable("FeV", lowBound=0, upBound=FeV_limit)
    FeNb = LpVariable("FeNb", lowBound=0, upBound=FeNb_limit)
    FeTi = LpVariable("FeTi", lowBound=0, upBound=FeTi_limit)
    FeMo = LpVariable("FeMo", lowBound=0, upBound=FeMo_limit)
    FeCrHC = LpVariable("FeCrHC", lowBound=0, upBound=FeCrHC_limit)
    FeCrLC = LpVariable("FeCrLC", lowBound=0, upBound=FeCrLC_limit)
    Cu = LpVariable("Cu", lowBound=0, upBound=Cu_limit)
    Ni = LpVariable("Ni", lowBound=0, upBound=Ni_limit)
    FeP = LpVariable("FeP", lowBound=0, upBound=FeP_limit)
    FeB_Wire = LpVariable("FeB_Wire", lowBound=0, upBound=FeB_Wire_limit)
    Si_Metal = LpVariable("Si_Metal", lowBound=0, upBound=Si_Metal_limit)
    Pure_Ca_Wire = LpVariable("Pure_Ca_Wire", lowBound=0, upBound=Pure_Ca_Wire_limit)
    CaSi_Wire = LpVariable("CaSi_Wire", lowBound=0, upBound=CaSi_Wire_limit)
    cafe_Wire = LpVariable("cafe_Wire", lowBound=0, upBound=cafe_Wire_limit)



    # Define the objective function
    prob1 += cost_df.loc["SiMn", "COST"] * SiMn + \
        cost_df.loc["HCMn", "COST"] * HCMn + \
        cost_df.loc["MCMn", "COST"] * MCMn + \
        cost_df.loc["LCMn", "COST"] * LCMn + \
        cost_df.loc["FeSi", "COST"] * FeSi + \
        cost_df.loc["MtMn", "COST"] * MtMn + \
        cost_df.loc["CPC", "COST"] * CPC + \
        cost_df.loc["ELCSiMn","COST"] * ELCSiMn + \
        cost_df.loc['GP','COST'] * GP + \
        cost_df.loc['FeV','COST'] * FeV + \
        cost_df.loc['FeNb','COST'] * FeNb + \
        cost_df.loc['FeTi','COST'] * FeTi + \
        cost_df.loc['FeMo','COST'] * FeMo + \
        cost_df.loc['FeCrHC','COST'] * FeCrHC + \
        cost_df.loc['FeCrLC','COST'] * FeCrLC + \
        cost_df.loc['Cu','COST'] * Cu + \
        cost_df.loc['Ni','COST'] * Ni + \
        cost_df.loc['FeP','COST'] * FeP + \
        cost_df.loc['FeB_Wire', 'COST'] * FeB_Wire + \
        cost_df.loc['Si_Metal', 'COST'] * Si_Metal + \
        cost_df.loc['Pure_Ca_Wire', 'COST'] * Pure_Ca_Wire + \
        cost_df.loc["CaSi_Wire", "COST"] * CaSi_Wire + \
        cost_df.loc["cafe_Wire", "COST"] * cafe_Wire

      #'''Define the constraints for each elements in ferroalloy'''

        # weight*recovery/100 of C in each ferro alloy
    prob1 += FA_df.loc['SiMn', 'C']*SiMn1*SiMn + \
        FA_df.loc['HCMn','C']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'C']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'C']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'C']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'C']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'C']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'C']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'C']*GP1*GP + \
        FA_df.loc['FeV', 'C']*FeV1*FeV + \
        FA_df.loc['FeNb', 'C']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'C']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'C']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'C']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'C']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'C']*Cu1*Cu + \
        FA_df.loc['Ni', 'C']*Ni1*Ni + \
        FA_df.loc['FeP', 'C']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'C']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'C']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'C']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'C']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'C']*cafe_Wire1*cafe_Wire == (filtered_df['c_aim'].iloc[0] - Carbon) * Tap_Weight * 10

# weight*recovery/100 of Si in each ferro alloy  
    prob1 += FA_df.loc['SiMn', 'Si']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Si']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Si']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Si']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Si']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Si']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Si']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Si']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Si']*GP1*GP + \
        FA_df.loc['FeV', 'Si']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Si']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Si']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Si']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Si']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Si']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Si']*Cu1*Cu + \
        FA_df.loc['Ni', 'Si']*Ni1*Ni + \
        FA_df.loc['FeP', 'Si']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Si']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Si']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Si']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Si']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Si']*cafe_Wire1*cafe_Wire  == (filtered_df['si_aim'].iloc[0] - Silicon) * Tap_Weight * 10

# weight*recovery/100 of Mn in each ferro alloy 
    prob1 += FA_df.loc['SiMn', 'Mn']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Mn']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Mn']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Mn']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Mn']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Mn']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Mn']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Mn']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Mn']*GP1*GP + \
        FA_df.loc['FeV', 'Mn']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Mn']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Mn']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Mn']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Mn']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Mn']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Mn']*Cu1*Cu + \
        FA_df.loc['Ni', 'Mn']*Ni1*Ni + \
        FA_df.loc['FeP', 'Mn']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Mn']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Mn']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Mn']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Mn']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Mn']*cafe_Wire1*cafe_Wire == (filtered_df['mn_aim'].iloc[0]- Manganese) * Tap_Weight * 10

 #weight*recovery/100 of P in each ferro alloy
    prob1 += FA_df.loc['SiMn', 'P']*SiMn1*SiMn + \
        FA_df.loc['HCMn','P']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'P']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'P']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'P']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'P']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'P']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'P']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'P']*GP1*GP + \
        FA_df.loc['FeV', 'P']*FeV1*FeV + \
        FA_df.loc['FeNb', 'P']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'P']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'P']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'P']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'P']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'P']*Cu1*Cu + \
        FA_df.loc['Ni', 'P']*Ni1*Ni + \
        FA_df.loc['FeP', 'P']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'P']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'P']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'P']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'P']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'P']*cafe_Wire1*cafe_Wire <= (filtered_df['p_aim'].iloc[0]- Phosphorus) * Tap_Weight * 10
    
# weight*recovery/100 of S in each ferro alloy0
    prob1 += FA_df.loc['SiMn', 'S']*SiMn1*SiMn + \
        FA_df.loc['HCMn','S']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'S']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'S']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'S']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'S']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'S']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'S']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'S']*GP1*GP + \
        FA_df.loc['FeV', 'S']*FeV1*FeV + \
        FA_df.loc['FeNb', 'S']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'S']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'S']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'S']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'S']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'S']*Cu1*Cu + \
        FA_df.loc['Ni', 'S']*Ni1*Ni + \
        FA_df.loc['FeP', 'S']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'S']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'S']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'S']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'S']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'S']*cafe_Wire1*cafe_Wire <= (filtered_df['s_aim'].iloc[0] - Sulphur) * Tap_Weight * 10

# weight*recovery/100 of V in each ferro alloy0
    prob1 += FA_df.loc['SiMn', 'V']*SiMn1*SiMn + \
        FA_df.loc['HCMn','V']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'V']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'V']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'V']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'V']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'V']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'V']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'V']*GP1*GP + \
        FA_df.loc['FeV', 'V']*FeV1*FeV + \
        FA_df.loc['FeNb', 'V']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'V']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'V']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'V']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'V']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'V']*Cu1*Cu + \
        FA_df.loc['Ni', 'V']*Ni1*Ni + \
        FA_df.loc['FeP', 'V']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'V']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'V']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'V']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'V']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'V']*cafe_Wire1*cafe_Wire <= (filtered_df['v_aim'].iloc[0] - Vanadium) * Tap_Weight * 10

# weight*recovery/100 of Nb in each ferro alloy0
    prob1 += FA_df.loc['SiMn', 'Nb']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Nb']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Nb']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Nb']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Nb']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Nb']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Nb']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Nb']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Nb']*GP1*GP + \
        FA_df.loc['FeV', 'Nb']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Nb']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Nb']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Nb']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Nb']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Nb']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Nb']*Cu1*Cu + \
        FA_df.loc['Ni', 'Nb']*Ni1*Ni + \
        FA_df.loc['FeP', 'Nb']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Nb']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Nb']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Nb']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Nb']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Nb']*cafe_Wire1*cafe_Wire <= (filtered_df['nb_aim'].iloc[0] - Niobium) * Tap_Weight * 10
    
# weight*recovery/100 of Ti in each ferro alloy0
    prob1 += FA_df.loc['SiMn', 'Ti']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Ti']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Ti']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Ti']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Ti']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Ti']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Ti']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Ti']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Ti']*GP1*GP + \
        FA_df.loc['FeV', 'Ti']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Ti']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Ti']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Ti']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Ti']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Ti']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Ti']*Cu1*Cu + \
        FA_df.loc['Ni', 'Ti']*Ni1*Ni + \
        FA_df.loc['FeP', 'Ti']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Ti']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Ti']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Ti']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Ti']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Ti']*cafe_Wire1*cafe_Wire <= (filtered_df['ti_aim'].iloc[0] - Titanium) * Tap_Weight * 10
    
# weight*recovery/100 of Mo in each ferro alloy0
    prob1 += FA_df.loc['SiMn', 'Mo']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Mo']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Mo']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Mo']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Mo']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Mo']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Mo']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Mo']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Mo']*GP1*GP + \
        FA_df.loc['FeV', 'Mo']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Mo']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Mo']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Mo']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Mo']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Mo']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Mo']*Cu1*Cu + \
        FA_df.loc['Ni', 'Mo']*Ni1*Ni + \
        FA_df.loc['FeP', 'Mo']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Mo']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Mo']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Mo']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Mo']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Mo']*cafe_Wire1*cafe_Wire <= (filtered_df['mo_aim'].iloc[0] - Molybdenum) * Tap_Weight * 10
    
# weight*recovery/100 of Cr in each ferro alloy0
    prob1 += FA_df.loc['SiMn', 'Cr']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Cr']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Cr']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Cr']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Cr']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Cr']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Cr']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Cr']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Cr']*GP1*GP + \
        FA_df.loc['FeV', 'Cr']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Cr']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Cr']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Cr']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Cr']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Cr']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Cr']*Cu1*Cu + \
        FA_df.loc['Ni', 'Cr']*Ni1*Ni + \
        FA_df.loc['FeP', 'Cr']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Cr']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Cr']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Cr']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Cr']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Cr']*cafe_Wire1*cafe_Wire <= (filtered_df['cr_aim'].iloc[0] - Chromium) * Tap_Weight * 10
    
# weight*recovery/100 of Cu in each ferro alloy0
    prob1 += FA_df.loc['SiMn', 'Cu']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Cu']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Cu']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Cu']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Cu']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Cu']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Cu']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Cu']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Cu']*GP1*GP + \
        FA_df.loc['FeV', 'Cu']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Cu']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Cu']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Cu']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Cu']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Cu']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Cu']*Cu1*Cu + \
        FA_df.loc['Ni', 'Cu']*Ni1*Ni + \
        FA_df.loc['FeP', 'Cu']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Cu']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Cu']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Cu']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Cu']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Cu']*cafe_Wire1*cafe_Wire <= (filtered_df['cu_aim'].iloc[0] - Copper) * Tap_Weight * 10
    
# weight*recovery/100 of Nickel in each ferro alloy0
    prob1 += FA_df.loc['SiMn', 'Ni']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Ni']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Ni']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Ni']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Ni']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Ni']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Ni']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Ni']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Ni']*GP1*GP + \
        FA_df.loc['FeV', 'Ni']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Ni']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Ni']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Ni']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Ni']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Ni']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Ni']*Cu1*Cu + \
        FA_df.loc['Ni', 'Ni']*Ni1*Ni + \
        FA_df.loc['FeP', 'Ni']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Ni']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Ni']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Ni']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Ni']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Ni']*cafe_Wire1*cafe_Wire <= (filtered_df['ni_aim'].iloc[0] - Nickel) * Tap_Weight * 10
    
# weight*recovery/100 of B (Boron) in each ferro alloy0
    prob1 += FA_df.loc['SiMn', 'B']*SiMn1*SiMn + \
        FA_df.loc['HCMn','B']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'B']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'B']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'B']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'B']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'B']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'B']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'B']*GP1*GP + \
        FA_df.loc['FeV', 'B']*FeV1*FeV + \
        FA_df.loc['FeNb', 'B']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'B']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'B']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'B']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'B']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'B']*Cu1*Cu + \
        FA_df.loc['Ni', 'B']*Ni1*Ni + \
        FA_df.loc['FeP', 'B']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'B']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'B']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'B']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'B']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'B']*cafe_Wire1*cafe_Wire <= (filtered_df['b_aim'].iloc[0] - Boron) * Tap_Weight * 10
    
# weight*recovery/100 of Ca (Calcium) in each ferro alloy0
    prob1 += FA_df.loc['SiMn', 'Ca']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Ca']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Ca']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Ca']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Ca']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Ca']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Ca']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Ca']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Ca']*GP1*GP + \
        FA_df.loc['FeV', 'Ca']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Ca']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Ca']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Ca']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Ca']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Ca']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Ca']*Cu1*Cu + \
        FA_df.loc['Ni', 'Ca']*Ni1*Ni + \
        FA_df.loc['FeP', 'Ca']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Ca']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Ca']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Ca']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Ca']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Ca']*cafe_Wire1*cafe_Wire <= (filtered_df['b_aim'].iloc[0] - Calcium) * Tap_Weight * 10

    prob1.solve()

# Print the results
    # if prob1.status == LpStatusInfeasible:
    #     infeasible_reasons = []
    #     for constraint in prob1.constraints.values():
    #         if not constraint.valid():
    #             infeasible_reasons.append(constraint.name)
    #     st.write("Status: Infeasible")
    #     st.write("Infeasible reasons:") 
    #     for reason in infeasible_reasons:
    #         st.write(reason)
    # else:
    #     st.write("Status:", LpStatus[prob1.status])

    st.write("Status: ", LpStatus[prob1.status] )
    st.write("Minimum cost = ", round(value(prob1.objective),0)) #, 'Thank You ! for saving Money :sparkling_heart:')
    st.write("SiMn = ", value(SiMn.varValue),"kg")
    st.write("HCMn = ", value(HCMn.varValue),"kg")
    st.write("MCMn = ", value(MCMn.varValue),"kg")
    st.write("LCMn = ", value(LCMn.varValue),"kg")
    st.write("MtMn = ", value(MtMn.varValue),"kg")
    st.write("FeSi = ", value(FeSi.varValue),"kg")
    st.write("CPC = ", value(CPC.varValue),"kg")
    st.write("ELCSiMn = ", value(ELCSiMn.varValue),"kg")
    st.write("GP = ", value(GP.varValue),"kg")
    st.write("FeV = ", value(FeV.varValue),"kg")
    st.write("FeNb = ", value(FeNb.varValue),"kg")
    st.write("FeTi = ", value(FeTi.varValue),"kg")
    st.write("FeMo = ", value(FeMo.varValue),"kg")
    st.write("FeCrHC = ", value(FeCrHC.varValue),"kg")
    st.write("FeCrLC = ", value(FeCrLC.varValue),"kg")
    st.write("Cu = ", value(Cu.varValue),"kg")
    st.write("Ni = ", value(Ni.varValue),"kg")
    st.write("FeP = ", value(FeP.varValue),"kg")
    st.write("FeB_Wire = ", value(FeB_Wire.varValue),"kg")
    st.write("Si_Metal = ", value(Si_Metal.varValue),"kg")
    st.write("Pure_Ca_Wire = ", value(Pure_Ca_Wire.varValue),"kg")
    st.write("CaSi_Wire = ", value(CaSi_Wire.varValue),"kg")
    st.write("cafe_Wire = ", value(cafe_Wire.varValue),"kg")

##############################this is all for maximum   ###########################

    # Define the objective function
    prob2 += cost_df.loc["SiMn", "COST"] * SiMn + \
        cost_df.loc["HCMn", "COST"] * HCMn + \
        cost_df.loc["MCMn", "COST"] * MCMn + \
        cost_df.loc["LCMn", "COST"] * LCMn + \
        cost_df.loc["FeSi", "COST"] * FeSi + \
        cost_df.loc["MtMn", "COST"] * MtMn + \
        cost_df.loc["CPC", "COST"] * CPC + \
        cost_df.loc["ELCSiMn","COST"] * ELCSiMn + \
        cost_df.loc['GP','COST'] * GP + \
        cost_df.loc['FeV','COST'] * FeV + \
        cost_df.loc['FeNb','COST'] * FeNb + \
        cost_df.loc['FeTi','COST'] * FeTi + \
        cost_df.loc['FeMo','COST'] * FeMo + \
        cost_df.loc['FeCrHC','COST'] * FeCrHC + \
        cost_df.loc['FeCrLC','COST'] * FeCrLC + \
        cost_df.loc['Cu','COST'] * Cu + \
        cost_df.loc['Ni','COST'] * Ni + \
        cost_df.loc['FeP','COST'] * FeP + \
        cost_df.loc['FeB_Wire', 'COST'] * FeB_Wire + \
        cost_df.loc['Si_Metal', 'COST'] * Si_Metal + \
        cost_df.loc['Pure_Ca_Wire', 'COST'] * Pure_Ca_Wire + \
        cost_df.loc["CaSi_Wire", "COST"] * CaSi_Wire + \
        cost_df.loc["cafe_Wire", "COST"] * cafe_Wire

      #'''Define the constraints for each elements in ferroalloy'''

        # weight*recovery/100 of C in each ferro alloy
    prob2 += FA_df.loc['SiMn', 'C']*SiMn1*SiMn + \
        FA_df.loc['HCMn','C']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'C']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'C']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'C']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'C']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'C']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'C']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'C']*GP1*GP + \
        FA_df.loc['FeV', 'C']*FeV1*FeV + \
        FA_df.loc['FeNb', 'C']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'C']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'C']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'C']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'C']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'C']*Cu1*Cu + \
        FA_df.loc['Ni', 'C']*Ni1*Ni + \
        FA_df.loc['FeP', 'C']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'C']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'C']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'C']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'C']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'C']*cafe_Wire1*cafe_Wire == (filtered_df['c_aim'].iloc[0] - Carbon) * Tap_Weight * 10

# weight*recovery/100 of Si in each ferro alloy  
    prob2 += FA_df.loc['SiMn', 'Si']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Si']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Si']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Si']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Si']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Si']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Si']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Si']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Si']*GP1*GP + \
        FA_df.loc['FeV', 'Si']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Si']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Si']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Si']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Si']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Si']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Si']*Cu1*Cu + \
        FA_df.loc['Ni', 'Si']*Ni1*Ni + \
        FA_df.loc['FeP', 'Si']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Si']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Si']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Si']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Si']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Si']*cafe_Wire1*cafe_Wire  == (filtered_df['si_aim'].iloc[0] - Silicon) * Tap_Weight * 10

# weight*recovery/100 of Mn in each ferro alloy 
    prob2 += FA_df.loc['SiMn', 'Mn']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Mn']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Mn']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Mn']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Mn']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Mn']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Mn']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Mn']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Mn']*GP1*GP + \
        FA_df.loc['FeV', 'Mn']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Mn']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Mn']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Mn']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Mn']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Mn']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Mn']*Cu1*Cu + \
        FA_df.loc['Ni', 'Mn']*Ni1*Ni + \
        FA_df.loc['FeP', 'Mn']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Mn']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Mn']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Mn']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Mn']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Mn']*cafe_Wire1*cafe_Wire == (filtered_df['mn_aim'].iloc[0]- Manganese) * Tap_Weight * 10

 #weight*recovery/100 of P in each ferro alloy
    prob2 += FA_df.loc['SiMn', 'P']*SiMn1*SiMn + \
        FA_df.loc['HCMn','P']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'P']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'P']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'P']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'P']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'P']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'P']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'P']*GP1*GP + \
        FA_df.loc['FeV', 'P']*FeV1*FeV + \
        FA_df.loc['FeNb', 'P']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'P']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'P']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'P']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'P']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'P']*Cu1*Cu + \
        FA_df.loc['Ni', 'P']*Ni1*Ni + \
        FA_df.loc['FeP', 'P']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'P']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'P']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'P']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'P']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'P']*cafe_Wire1*cafe_Wire <= (filtered_df['p_aim'].iloc[0]- Phosphorus) * Tap_Weight * 10
    
# weight*recovery/100 of S in each ferro alloy0
    prob2 += FA_df.loc['SiMn', 'S']*SiMn1*SiMn + \
        FA_df.loc['HCMn','S']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'S']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'S']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'S']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'S']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'S']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'S']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'S']*GP1*GP + \
        FA_df.loc['FeV', 'S']*FeV1*FeV + \
        FA_df.loc['FeNb', 'S']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'S']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'S']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'S']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'S']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'S']*Cu1*Cu + \
        FA_df.loc['Ni', 'S']*Ni1*Ni + \
        FA_df.loc['FeP', 'S']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'S']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'S']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'S']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'S']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'S']*cafe_Wire1*cafe_Wire <= (filtered_df['s_aim'].iloc[0] - Sulphur) * Tap_Weight * 10

# weight*recovery/100 of V in each ferro alloy0
    prob2 += FA_df.loc['SiMn', 'V']*SiMn1*SiMn + \
        FA_df.loc['HCMn','V']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'V']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'V']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'V']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'V']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'V']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'V']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'V']*GP1*GP + \
        FA_df.loc['FeV', 'V']*FeV1*FeV + \
        FA_df.loc['FeNb', 'V']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'V']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'V']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'V']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'V']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'V']*Cu1*Cu + \
        FA_df.loc['Ni', 'V']*Ni1*Ni + \
        FA_df.loc['FeP', 'V']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'V']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'V']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'V']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'V']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'V']*cafe_Wire1*cafe_Wire <= (filtered_df['v_aim'].iloc[0] - Vanadium) * Tap_Weight * 10

# weight*recovery/100 of Nb in each ferro alloy0
    prob2 += FA_df.loc['SiMn', 'Nb']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Nb']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Nb']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Nb']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Nb']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Nb']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Nb']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Nb']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Nb']*GP1*GP + \
        FA_df.loc['FeV', 'Nb']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Nb']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Nb']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Nb']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Nb']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Nb']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Nb']*Cu1*Cu + \
        FA_df.loc['Ni', 'Nb']*Ni1*Ni + \
        FA_df.loc['FeP', 'Nb']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Nb']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Nb']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Nb']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Nb']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Nb']*cafe_Wire1*cafe_Wire <= (filtered_df['nb_aim'].iloc[0] - Niobium) * Tap_Weight * 10
    
# weight*recovery/100 of Ti in each ferro alloy0
    prob2 += FA_df.loc['SiMn', 'Ti']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Ti']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Ti']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Ti']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Ti']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Ti']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Ti']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Ti']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Ti']*GP1*GP + \
        FA_df.loc['FeV', 'Ti']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Ti']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Ti']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Ti']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Ti']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Ti']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Ti']*Cu1*Cu + \
        FA_df.loc['Ni', 'Ti']*Ni1*Ni + \
        FA_df.loc['FeP', 'Ti']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Ti']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Ti']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Ti']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Ti']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Ti']*cafe_Wire1*cafe_Wire <= (filtered_df['ti_aim'].iloc[0] - Titanium) * Tap_Weight * 10
    
# weight*recovery/100 of Mo in each ferro alloy0
    prob2 += FA_df.loc['SiMn', 'Mo']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Mo']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Mo']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Mo']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Mo']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Mo']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Mo']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Mo']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Mo']*GP1*GP + \
        FA_df.loc['FeV', 'Mo']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Mo']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Mo']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Mo']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Mo']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Mo']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Mo']*Cu1*Cu + \
        FA_df.loc['Ni', 'Mo']*Ni1*Ni + \
        FA_df.loc['FeP', 'Mo']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Mo']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Mo']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Mo']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Mo']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Mo']*cafe_Wire1*cafe_Wire <= (filtered_df['mo_aim'].iloc[0] - Molybdenum) * Tap_Weight * 10
    
# weight*recovery/100 of Cr in each ferro alloy0
    prob2 += FA_df.loc['SiMn', 'Cr']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Cr']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Cr']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Cr']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Cr']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Cr']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Cr']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Cr']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Cr']*GP1*GP + \
        FA_df.loc['FeV', 'Cr']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Cr']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Cr']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Cr']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Cr']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Cr']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Cr']*Cu1*Cu + \
        FA_df.loc['Ni', 'Cr']*Ni1*Ni + \
        FA_df.loc['FeP', 'Cr']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Cr']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Cr']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Cr']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Cr']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Cr']*cafe_Wire1*cafe_Wire <= (filtered_df['cr_aim'].iloc[0] - Chromium) * Tap_Weight * 10
    
# weight*recovery/100 of Cu in each ferro alloy0
    prob2 += FA_df.loc['SiMn', 'Cu']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Cu']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Cu']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Cu']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Cu']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Cu']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Cu']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Cu']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Cu']*GP1*GP + \
        FA_df.loc['FeV', 'Cu']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Cu']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Cu']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Cu']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Cu']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Cu']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Cu']*Cu1*Cu + \
        FA_df.loc['Ni', 'Cu']*Ni1*Ni + \
        FA_df.loc['FeP', 'Cu']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Cu']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Cu']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Cu']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Cu']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Cu']*cafe_Wire1*cafe_Wire <= (filtered_df['cu_aim'].iloc[0] - Copper) * Tap_Weight * 10
    
# weight*recovery/100 of Nickel in each ferro alloy0
    prob2 += FA_df.loc['SiMn', 'Ni']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Ni']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Ni']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Ni']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Ni']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Ni']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Ni']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Ni']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Ni']*GP1*GP + \
        FA_df.loc['FeV', 'Ni']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Ni']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Ni']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Ni']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Ni']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Ni']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Ni']*Cu1*Cu + \
        FA_df.loc['Ni', 'Ni']*Ni1*Ni + \
        FA_df.loc['FeP', 'Ni']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Ni']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Ni']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Ni']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Ni']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Ni']*cafe_Wire1*cafe_Wire <= (filtered_df['ni_aim'].iloc[0] - Nickel) * Tap_Weight * 10
    
# weight*recovery/100 of B (Boron) in each ferro alloy0
    prob2 += FA_df.loc['SiMn', 'B']*SiMn1*SiMn + \
        FA_df.loc['HCMn','B']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'B']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'B']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'B']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'B']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'B']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'B']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'B']*GP1*GP + \
        FA_df.loc['FeV', 'B']*FeV1*FeV + \
        FA_df.loc['FeNb', 'B']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'B']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'B']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'B']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'B']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'B']*Cu1*Cu + \
        FA_df.loc['Ni', 'B']*Ni1*Ni + \
        FA_df.loc['FeP', 'B']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'B']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'B']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'B']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'B']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'B']*cafe_Wire1*cafe_Wire <= (filtered_df['b_aim'].iloc[0] - Boron) * Tap_Weight * 10
    
# weight*recovery/100 of Ca (Calcium) in each ferro alloy0
    prob2 += FA_df.loc['SiMn', 'Ca']*SiMn1*SiMn + \
        FA_df.loc['HCMn','Ca']*HCMn1*HCMn + \
        FA_df.loc['MCMn', 'Ca']*MCMn1*MCMn + \
        FA_df.loc['LCMn', 'Ca']*LCMn1*LCMn + \
        FA_df.loc['FeSi', 'Ca']*FeSi1*FeSi  + \
        FA_df.loc['MtMn', 'Ca']*MtMn1*MtMn + \
        FA_df.loc['CPC', 'Ca']*CPC1*CPC + \
        FA_df.loc['ELCSiMn', 'Ca']*ELCSiMn1*ELCSiMn + \
        FA_df.loc['GP', 'Ca']*GP1*GP + \
        FA_df.loc['FeV', 'Ca']*FeV1*FeV + \
        FA_df.loc['FeNb', 'Ca']*FeNb1*FeNb + \
        FA_df.loc['FeTi', 'Ca']*FeTi1*FeTi + \
        FA_df.loc['FeMo', 'Ca']*FeMo1*FeMo + \
        FA_df.loc['FeCrHC', 'Ca']*FeCrHC1*FeCrHC + \
        FA_df.loc['FeCrLC', 'Ca']*FeCrLC1*FeCrLC + \
        FA_df.loc['Cu', 'Ca']*Cu1*Cu + \
        FA_df.loc['Ni', 'Ca']*Ni1*Ni + \
        FA_df.loc['FeP', 'Ca']*FeP1*FeP + \
        FA_df.loc['FeB_Wire', 'Ca']*FeB_Wire1*FeB_Wire + \
        FA_df.loc['Si_Metal', 'Ca']*Si_Metal1*Si_Metal + \
        FA_df.loc['Pure_Ca_Wire', 'Ca']*Pure_Ca_Wire1*Pure_Ca_Wire + \
        FA_df.loc['CaSi_Wire', 'Ca']*CaSi_Wire1*CaSi_Wire + \
        FA_df.loc['cafe_Wire', 'Ca']*cafe_Wire1*cafe_Wire <= (filtered_df['b_aim'].iloc[0] - Calcium) * Tap_Weight * 10
    
    # if filtered_df['si_aim'].iloc[0]  == 0:
    #     #fix simn zero  
    #     filtered_df['si_aim'].iloc[0] = 0.008

    # # elif filtered_df['si_aim'].iloc[0] <= 0.010:
    #     # SiMn.varValue = 0
    #     # FeSi.varValue = 0
    # else: 
    #     filtered_df['si_aim'].iloc[0] = filtered_df['si_aim'].iloc[0]
    #     #SiMn.varValue = 0

    prob2.solve()

# contraint for reason
    # if prob2.status == LpStatusInfeasible:
    #     infeasible_reasons = []
    #     for constraint in prob2.constraints.values():
    #         if not constraint.valid():
    #             infeasible_reasons.append(constraint.name)
    #     st.write("Status: Infeasible")
    #     st.write("Infeasible reasons:") 
    #     for reason in infeasible_reasons:
    #         st.write(reason)
    # else:
    #     st.write("Status:", LpStatus[prob2.status])
# Print the results MAXIMUM
    st.write("Status: ", LpStatus[prob2.status] )
    st.write("Maximum cost = ", round(value(prob2.objective),0)) #, 'Thank You ! for saving Money :sparkling_heart:')
    st.write("SiMn = ", value(SiMn.varValue),"kg")
    st.write("HCMn = ", value(HCMn.varValue),"kg")
    st.write("MCMn = ", value(MCMn.varValue),"kg")
    st.write("LCMn = ", value(LCMn.varValue),"kg")
    st.write("MtMn = ", value(MtMn.varValue),"kg")
    st.write("FeSi = ", value(FeSi.varValue),"kg")
    st.write("CPC = ", value(CPC.varValue),"kg")
    st.write("ELCSiMn = ", value(ELCSiMn.varValue),"kg")
    st.write("GP = ", value(GP.varValue),"kg")
    st.write("FeV = ", value(FeV.varValue),"kg")
    st.write("FeNb = ", value(FeNb.varValue),"kg")
    st.write("FeTi = ", value(FeTi.varValue),"kg")
    st.write("FeMo = ", value(FeMo.varValue),"kg")
    st.write("FeCrHC = ", value(FeCrHC.varValue),"kg")
    st.write("FeCrLC = ", value(FeCrLC.varValue),"kg")
    st.write("Cu = ", value(Cu.varValue),"kg")
    st.write("Ni = ", value(Ni.varValue),"kg")
    st.write("FeP = ", value(FeP.varValue),"kg")
    st.write("FeB_Wire = ", value(FeB_Wire.varValue),"kg")
    st.write("Si_Metal = ", value(Si_Metal.varValue),"kg")
    st.write("Pure_Ca_Wire = ", value(Pure_Ca_Wire.varValue),"kg")
    st.write("CaSi_Wire = ", value(CaSi_Wire.varValue),"kg")
    st.write("cafe_Wire = ", value(cafe_Wire.varValue),"kg")
    # if status == pulp.LpStatusInfeasible:
    #     st.write('The problem is infeasible. The following contrain is not satisfied:')
    #     for constraint in prob2.constraints:
    #         if constraint.status == pulp.LpConstraintNotSatisfied:
    #             st.write(constraint.name)



    # Collect results
    result_min = {
        'Objective': 'Minimize',
        'SiMn': SiMn.varValue,
        'HCMn': HCMn.varValue,
        'MCMn': MCMn.varValue,
        'LCMn': LCMn.varValue,
        'Total Cost': pulp.value(prob1.objective),
        'Status': LpStatus[prob1.status]
    }

    result_max = {
        'Objective': 'Maximize',
        'SiMn': SiMn.varValue,
        'HCMn': HCMn.varValue,
        'MCMn': MCMn.varValue,
        'LCMn': LCMn.varValue,
        'Total Cost': pulp.value(prob2.objective),
        'Status': LpStatus[prob2.status]
    }

    return result_min, result_max

# List to store results
results = []

# Define different sets of parameters to run the problem multiple times
parameters = [
    (100, 100, 100, 100, 0.9, 0.8, 0.85, 0.75),
    (150, 120, 110, 130, 0.85, 0.75, 0.8, 0.7),
    (200, 140, 130, 150, 0.8, 0.7, 0.75, 0.65),
    # Add more sets of parameters as needed
]

# Run the problem multiple times with different parameters
for params in parameters:
    result_min, result_max = model(*params)
    results.append(result_min)
    results.append(result_max)

# Create a DataFrame to hold the results
df = pd.DataFrame(results)

# Save the DataFrame to an Excel sheet
df.to_excel('optimization_results.xlsx', index=False)

print("Results saved to optimization_results.xlsx")






# Create a column for each elements
container = st.container()
with st.container():
    df = pd.read_excel(r'D:\#arjun\FA model\grade.xlsx')
    df['Dolvi grades'] = df['Dolvi grades'].str.upper()

    grade = st.selectbox('Select Grade', df['Dolvi grades'].unique())
    filtered_df = df[df['Dolvi grades'].str.upper() == grade.upper()]
    carbon_value = filtered_df['c_blow_end'].iloc[0]

# all the conditions which causes infeasible reasult
    if filtered_df['si_aim'].iloc[0]  == 0:
       #fix simn zero
       filtered_df['si_aim'].iloc[0] = 0.005
    else: 
       filtered_df['si_aim'].iloc[0] = filtered_df['si_aim'].iloc[0]

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
        'Ca': [filtered_df['ca_min'].iloc[0], filtered_df['ca_max'].iloc[0], filtered_df['ca_aim'].iloc[0]],
        'Ni': [filtered_df['ni_min'].iloc[0], filtered_df['ni_max'].iloc[0], filtered_df['ni_aim'].iloc[0]]
    })

    st.write(min_max_df[['Elements', 'C', 'Mn', 'S', 'P', 'Si', 'Al', 'Cr', 'Cu', 'V', 'Ti', 'Nb', 'Mo', 'B', 'Ca', 'Ni']])
    st.markdown("<h2 style='text-align: left; color: white; font-size: 15px;'>Enter the blow end chemistry</h2>", unsafe_allow_html=True)
    container = st.container()

    col1, col2, col3,  = container.columns(3)
    
    Carbon = col1.number_input("C", format="%.3f", value= carbon_value)
    Manganese = col2.number_input("Mn", format="%.3f")
    Sulphur = col3.number_input("S", format="%.3f")

    col4, col5,col6, = container.columns(3)
    Phosphorus = col4.number_input("P", format="%.3f")
    Silicon = col5.number_input("Si", format="%.3f")
    Tap_Weight = col6.number_input("Tap_Weight", value=350)

    col7, col8,col9, = container.columns(3)
    Vanadium = col7.number_input("V", format="%.3f")
    Niobium = col8.number_input("Nb", format="%.3f")
    Titanium = col9.number_input("Ti", format="%.3f")

    col10, col11,col12, = container.columns(3)
    Copper = col10.number_input("Cu", format="%.3f")
    Molybdenum = col11.number_input("Mo", format="%.3f")
    Chromium = col12.number_input("Cr", format="%.3f")

    col13, col14,col15, = container.columns(3)
    Nickel = col10.number_input("Ni", format="%.3f")
    Boron = col11.number_input("B", format="%.3f")
    Calcium = col12.number_input("Ca", format="%.3f")

    # min_max_df.at[2, 'C'] = Carbon
    # min_max_df.at[2, 'Mn'] = Manganese
    # min_max_df.at[2, 'S'] = Sulphur
    # min_max_df.at[2, 'P'] = Phosphorus    
    # min_max_df.at[2, 'Si'] = Silicon

    if Carbon > filtered_df['c_aim'].iloc[0]:
        filtered_df['c_aim'].iloc[0] = filtered_df['c_max'].iloc[0]
        #filtered_df['c_max'].iloc[0] = filtered_df['c_aim'].iloc[0]
    else: 
        Carbon = Carbon
        
#siderbar function
    with st.sidebar:    
        st.subheader("Availibility of bunkers:")
    
        col1, col2 = st.columns(2)
        col1.write("Materials")
        SiMn1 = col1.number_input("SiMn1", min_value=0.0, max_value=1.0, value=1.0 , step = 1.0)
        HCMn1 = col1.number_input("HCMn1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        MCMn1 = col1.number_input("MCMn1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        LCMn1 = col1.number_input("LCMn1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        MtMn1 = col1.number_input("MtMn1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        FeSi1 = col1.number_input("FeSi1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        CPC1 = col1.number_input("CPC1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        GP1 = col1.number_input("GP1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        ELCSiMn1 = col1.number_input("ELCSiMn1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        FeV1 = col1.number_input("FeV1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        FeNb1 = col1.number_input("FeNb1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        FeTi1 = col1.number_input("FeTi1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        FeMo1 = col1.number_input("FeMo1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        FeCrHC1 = col1.number_input("FeCrHC1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        FeCrLC1 = col1.number_input("FeCrLC1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        Cu1 = col1.number_input("Cu1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        Ni1 = col1.number_input("Ni1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        FeP1 = col1.number_input("FeP1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        FeB_Wire1 = col1.number_input("FeB_Wire1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        Si_Metal1 = col1.number_input("Si_Metal1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        Pure_Ca_Wire1 = col1.number_input("Pure_Ca_Wire1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        CaSi_Wire1 = col1.number_input("CaSi_Wire1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)
        cafe_Wire1 = col1.number_input("cafe_Wire1", min_value=0.0, max_value=1.0, value=1.0, step = 1.0)

        col2.write("Limit")  # Add an empty slot to create space between the two columns
        SiMn_limit = col2.number_input("SiMn_Limit",value=9999, max_value=9999)
        HCMn_limit = col2.number_input("HCMn_Limit",value=9999, max_value=9999)
        MCMn_limit = col2.number_input("MCMn_Limit",value=9999, max_value=9999)
        LCMn_limit = col2.number_input("LCMn_Limit",value=9999, max_value=9999)
        MtMn_limit = col2.number_input("MtMn_Limit",value=9999, max_value=9999)
        FeSi_limit = col2.number_input("FeSi_Limit",value=9999, max_value=9999)
        CPC_limit = col2.number_input("CPC_Limit",value=9999, max_value=9999)
        GP_limit = col2.number_input("GP_Limit",value=9999, max_value=9999)
        ELCSiMn_limit = col2.number_input("ELCSiMn_Limit",value=9999, max_value=9999)
        FeV_limit = col2.number_input("FeV_Limit",value=9999, max_value=9999)
        FeNb_limit = col2.number_input("FeNb_Limit",value=9999, max_value=9999)
        FeTi_limit = col2.number_input("FeTi_Limit",value=9999, max_value=9999)
        FeMo_limit = col2.number_input("FeMo_Limit",value=9999, max_value=9999)
        FeCrHC_limit = col2.number_input("FeCrHC_Limit",value=9999, max_value=9999)
        FeCrLC_limit = col2.number_input("FeCrLC_Limit",value=9999, max_value=9999)
        Cu_limit = col2.number_input("Cu_Limit",value=9999, max_value=9999)
        Ni_limit = col2.number_input("Ni_Limit",value=9999, max_value=9999)
        FeP_limit = col2.number_input("FeP_Limit",value=9999, max_value=9999)
        FeB_Wire_limit = col2.number_input("FeB_Wire_Limit",value=9999, max_value=9999)
        Si_Metal_limit = col2.number_input("Si_Metal_Limit",value=9999, max_value=9999)
        Pure_Ca_Wire_limit = col2.number_input("Pure_Ca_Wire_Limit",value=9999, max_value=9999)
        CaSi_Wire_limit = col2.number_input("CaSi_Wire_Limit",value=9999, max_value=9999)
        cafe_Wire_limit = col2.number_input("cafe_Wire_Limit",value=9999, max_value=9999)

        if SiMn1  == 0:
            SiMn_limit = 0
        else:
            SiMn_limit = SiMn_limit
        if HCMn1 == 0:
            HCMn_limit = 0
        else:
            HCMn_limit = HCMn_limit
        if MCMn1 == 0:
            MCMn_limit = 0
        else:
            MCMn_limit = MCMn_limit
        if LCMn1 == 0:
            LCMn_limit = 0
        else:
            LCMn_limit = LCMn_limit
        if MtMn1 == 0:
            MtMn_limit = 0
        else:
            MtMn_limit = MtMn_limit
        if CPC1 == 0:
            CPC_limit = 0
        else:
            CPC_limit = CPC_limit

if st.button("Predict"):
    # Call your function
    model() 
