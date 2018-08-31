from board import Board
from hand import Hand
from showdown_strengths.flush import flush_of
from showdown_strengths.four_of_a_kind import four_of_a_kind_of
from showdown_strengths.full_house import full_house_of
from showdown_strengths.high_card import high_card_of
from showdown_strengths.pair import pair_of
from showdown_strengths.straight import straight_of
from showdown_strengths.straight_flush import straight_flush_of
from showdown_strengths.three_of_a_kind import three_of_a_kind_of
from showdown_strengths.two_pair import two_pair_of


def showdown_value_of(hand: Hand, board: Board):
    for f in [straight_flush_of, four_of_a_kind_of, full_house_of,
              flush_of, straight_of, three_of_a_kind_of, two_pair_of,
              pair_of, high_card_of]:
        result = f(hand, board)
        if result is not None:
            return result
