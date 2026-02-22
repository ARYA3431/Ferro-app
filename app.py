def model():

    # taking cost details from sheet as Dataframe
    cost_df = pd.read_excel('details.xlsx', sheet_name='cost', index_col=0)

    # taking Ferro alloy details from sheet as Dataframe
    FA_df = pd.read_excel('details.xlsx', sheet_name='FA_details')
    FA_df.set_index('Ferroalloy', inplace=True)

    # Define the problem
    prob1 = LpProblem("LP Problem", LpMinimize)
    prob2 = LpProblem("LP Problem", LpMaximize)

    # ---------------- VARIABLES ----------------
    SiMn = LpVariable("SiMn", lowBound=0, upBound=SiMn_limit)
    HCMn = LpVariable("HCMn", lowBound=0, upBound=HCMn_limit)
    MCMn = LpVariable("MCMn", lowBound=0, upBound=MCMn_limit)
    LCMn = LpVariable("LCMn", lowBound=0, upBound=LCMn_limit)
    MtMn = LpVariable("MtMn", lowBound=0, upBound=MtMn_limit)
    FeSi = LpVariable("FeSi", lowBound=0, upBound=FeSi_limit)
    CPC  = LpVariable("CPC",  lowBound=0, upBound=CPC_limit)
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

    # ---------------- OBJECTIVE (MIN COST) ----------------
    prob1 += (
        cost_df.loc["SiMn", "COST"] * SiMn +
        cost_df.loc["HCMn", "COST"] * HCMn +
        cost_df.loc["MCMn", "COST"] * MCMn +
        cost_df.loc["LCMn", "COST"] * LCMn +
        cost_df.loc["FeSi", "COST"] * FeSi +
        cost_df.loc["MtMn", "COST"] * MtMn +
        cost_df.loc["CPC", "COST"] * CPC +
        cost_df.loc["ELCSiMn", "COST"] * ELCSiMn +
        cost_df.loc["GP", "COST"] * GP +
        cost_df.loc["FeV", "COST"] * FeV +
        cost_df.loc["FeNb", "COST"] * FeNb +
        cost_df.loc["FeTi", "COST"] * FeTi +
        cost_df.loc["FeMo", "COST"] * FeMo +
        cost_df.loc["FeCrHC", "COST"] * FeCrHC +
        cost_df.loc["FeCrLC", "COST"] * FeCrLC +
        cost_df.loc["Cu", "COST"] * Cu +
        cost_df.loc["Ni", "COST"] * Ni +
        cost_df.loc["FeP", "COST"] * FeP +
        cost_df.loc["FeB_Wire", "COST"] * FeB_Wire +
        cost_df.loc["Si_Metal", "COST"] * Si_Metal +
        cost_df.loc["Pure_Ca_Wire", "COST"] * Pure_Ca_Wire +
        cost_df.loc["CaSi_Wire", "COST"] * CaSi_Wire +
        cost_df.loc["cafe_Wire", "COST"] * cafe_Wire
    )

    # ---------------- SOLVE ----------------
    prob1.solve()

    # ---------------- OUTPUT ----------------
    st.write("Status:", LpStatus[prob1.status])
    st.write("Minimum cost =", round(value(prob1.objective), 0))

    for v in prob1.variables():
        st.write(v.name, "=", round(value(v), 3), "kg")