import streamlit as st


def show_metrics(
    total_bets,
    win_rate,
    roi,
    total_profit,
    winning_bets,
    losing_bets,
    total_stake,
    total_returns,
):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Bets",
        f"{total_bets:,}"
    )

    c2.metric(
        "Win Rate",
        f"{win_rate:.2f}%"
    )

    c3.metric(
        "ROI",
        f"{roi:.2f}%"
    )

    c4.metric(
        "Net Profit",
        f"KES {total_profit:,.2f}"
    )

    c5, c6, c7, c8 = st.columns(4)

    c5.metric(
        "Winning Bets",
        winning_bets
    )

    c6.metric(
        "Losing Bets",
        losing_bets
    )

    c7.metric(
        "Total Stake",
        f"KES {total_stake:,.2f}"
    )

    c8.metric(
        "Total Returns",
        f"KES {total_returns:,.2f}"
    )