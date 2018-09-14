from order_poker_hands import get_top_x_percent_of_hands
from range_battle import range_battle


def call_equity(hand, steal):
    sb_range = list(get_top_x_percent_of_hands(steal))
    equity_on_the_flop = range_battle([hand], sb_range)
    return 5 * equity_on_the_flop - 2.5


def fold_equity():
    return -1


def three_bet_equity(hand, steal, fold_percentage):
    # If he folds, we win 2.5
    equity = fold_percentage / 100 * 2.5

    # If he calls
    sb_call_range = list(get_top_x_percent_of_hands(steal * (100 - fold_percentage) / 100))
    equity_on_the_flop = range_battle([hand], sb_call_range)
    equity += (100 - fold_percentage) / 100 * (16 * equity_on_the_flop - 8)
    return equity
