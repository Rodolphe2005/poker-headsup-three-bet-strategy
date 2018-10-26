from order_poker_hands import get_top_x_percent_of_hands
from range_battle import range_battle


def call_equity(hand, steal, oop_penalty, steal_size):
    sb_range = list(get_top_x_percent_of_hands(steal))
    equity_on_the_flop = range_battle([hand], sb_range)
    return 2 * steal_size * (equity_on_the_flop * (100-oop_penalty)/100) - steal_size


def fold_equity():
    return -1


def three_bet_equity(*, hand, steal, fold_percentage, fourbet, oop_penalty, steal_size, threebet_size):
    # If he folds, we win 2.5
    fold_equity = fold_percentage / 100 * steal_size

    # If he calls
    # TODO Remove the top percent that corresponds to his 4Bet range
    sb_call_range = list(get_top_x_percent_of_hands(steal * (100 - fold_percentage) / 100))
    equity_on_the_flop = range_battle([hand], sb_call_range) * (100-oop_penalty)/100
    call_equity = (100 - fold_percentage - fourbet) / 100 * (
            2 * threebet_size * equity_on_the_flop - threebet_size)

    # If he 4bets, we suppose that we always fold
    four_bet_equity = fourbet / 100 * -threebet_size
    return fold_equity + call_equity + four_bet_equity
