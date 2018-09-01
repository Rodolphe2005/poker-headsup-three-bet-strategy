from collections import Counter

from hand_battle.board import Board
from hand_battle.hand import Hand
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
    card_number_counter = Counter([card.number for card in hand.cards + board.cards])

    result = straight_flush_of(hand, board, card_number_counter=card_number_counter)
    if result is not None:
        return result

    result = four_of_a_kind_of(hand, board, card_number_counter=card_number_counter)
    if result is not None:
        return result


    result = full_house_of(hand, board, card_number_counter=card_number_counter)
    if result is not None:
        return result


    result = flush_of(hand, board, card_number_counter=card_number_counter)
    if result is not None:
        return result


    result = straight_of(hand, board, card_number_counter=card_number_counter)
    if result is not None:
        return result


    result = three_of_a_kind_of(hand, board, card_number_counter=card_number_counter)
    if result is not None:
        return result

    result = two_pair_of(hand, board, card_number_counter=card_number_counter)
    if result is not None:
        return result

    result = pair_of(hand, board, card_number_counter=card_number_counter)
    if result is not None:
        return result

    result = high_card_of(hand, board, card_number_counter=card_number_counter)
    if result is not None:
        return result

    assert False