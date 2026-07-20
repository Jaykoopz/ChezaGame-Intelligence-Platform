import pandas as pd
import streamlit as st


@st.cache_data
def load_database(file):
    """
    Loads the ChezaGame database from Excel.
    """

    bets = pd.read_excel(
        file,
        sheet_name="Bets"
    )

    selections = pd.read_excel(
        file,
        sheet_name="Selections"
    )

    return bets, selections