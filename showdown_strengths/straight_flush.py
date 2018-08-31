from typing import List

from board import Board
from card import Card
from hand import Hand
from showdown_strengths.flush import flush_of
from showdown_strengths.straight import straight_of


class StraightFlush:
    ranking = 9

    def __init__(self, card_name: str):
        self.card = Card(card_name)

    def __lt__(self, other):
        return self.card.number < other.card.number

    def __eq__(self, other):
        return self.card == other.card


def straight_flush_of(hand: Hand, board: Board):
    if flush_of(hand, board) is None or straight_of(hand, board) is None:
        return None
    else:
        cards = hand.cards + board.cards
        for card in cards:
            if card.number.value > 5:
                if all(card.decrease(i) in cards for i in range(1, 5)):
                    return StraightFlush(card.name)
            elif card.number.value == 5:
                if all(card.decrease(i) in cards for i in range(1, 4)) and Card('A' + card.suit) in cards:
                    return StraightFlush(card.name)
            else:
                continue
        else:
            return None
