import streamlit as st


def show_filters(bets):
    st.sidebar.header("Filters")

    # Bet Result Filter
    results = sorted(
        bets["result"].dropna().unique()
    )

    selected_results = st.sidebar.multiselect(
        "Bet Result",
        results,
        default=results
    )

    # Stake Filter
    min_stake = float(bets["stake"].min())
    max_stake = float(bets["stake"].max())

    stake_range = st.sidebar.slider(
        "Stake Range (KES)",
        min_value=min_stake,
        max_value=max_stake,
        value=(min_stake, max_stake)
    )

    # Odds Filter
    min_odds = float(bets["total_odds"].min())
    max_odds = float(bets["total_odds"].max())

    odds_range = st.sidebar.slider(
        "Odds Range",
        min_value=min_odds,
        max_value=max_odds,
        value=(min_odds, max_odds)
    )

    return (
        selected_results,
        stake_range,
        odds_range
    )