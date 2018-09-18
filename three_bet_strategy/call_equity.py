from order_poker_hands import get_top_x_percent_of_hands
from range_battle import range_battle


raise_size = 2.5
three_bet_size = 8
four_bet_percentage = 10

def call_equity(hand, steal):
    sb_range = list(get_top_x_percent_of_hands(steal))
    equity_on_the_flop = range_battle([hand], sb_range)
    return 2 * raise_size * equity_on_the_flop - raise_size


def fold_equity():
    return -1


def three_bet_equity(hand, steal, fold_percentage):
    # If he folds, we win 2.5
    equity = fold_percentage / 100 * raise_size

    # If he calls
    # TODO Remove the top percent that corresponds to his 4Bet range
    sb_call_range = list(get_top_x_percent_of_hands(steal * (100 - fold_percentage) / 100))
    equity_on_the_flop = range_battle([hand], sb_call_range)
    equity += (100 - fold_percentage - four_bet_percentage) / 100 * (2 * three_bet_size * equity_on_the_flop - three_bet_size)

    # If he 4bets, we suppose that we always fold
    equity -= four_bet_percentage/100 * three_bet_size
    return equity
