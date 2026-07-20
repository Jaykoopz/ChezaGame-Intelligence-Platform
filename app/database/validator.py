import streamlit as st


REQUIRED_BETS_COLUMNS = [
    "bet_id",
    "date",
    "stake",
    "total_odds",
    "returns",
    "profit",
    "result",
    "selections",
]

REQUIRED_SELECTION_COLUMNS = [
    "Bet ID",
    "Match",
    "Market",
    "Outcome",
]


def validate_database(bets, selections):

    missing_bets = [
        col
        for col in REQUIRED_BETS_COLUMNS
        if col not in bets.columns
    ]

    missing_selections = [
        col
        for col in REQUIRED_SELECTION_COLUMNS
        if col not in selections.columns
    ]

    if missing_bets:

        st.error(
            f"❌ Bets sheet is missing: {', '.join(missing_bets)}"
        )

        return False

    if missing_selections:

        st.error(
            f"❌ Selections sheet is missing: {', '.join(missing_selections)}"
        )

        return False

    return True