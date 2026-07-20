def calculate_kpis(bets):

    total_bets = len(bets)

    winning_bets = len(
        bets[bets["profit"] > 0]
    )

    losing_bets = len(
        bets[bets["profit"] <= 0]
    )

    total_stake = bets["stake"].sum()

    total_returns = bets["returns"].sum()

    total_profit = bets["profit"].sum()

    average_stake = bets["stake"].mean()

    average_odds = bets["total_odds"].mean()

    roi = 0

    if total_stake > 0:

        roi = (
            total_profit / total_stake
        ) * 100

    win_rate = 0

    if total_bets > 0:

        win_rate = (
            winning_bets / total_bets
        ) * 100

    return {

        "total_bets": total_bets,

        "winning_bets": winning_bets,

        "losing_bets": losing_bets,

        "total_stake": total_stake,

        "total_returns": total_returns,

        "total_profit": total_profit,

        "average_stake": average_stake,

        "average_odds": average_odds,

        "roi": roi,

        "win_rate": win_rate,

    }