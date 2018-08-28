from typing import List

from card import Card
from hand import Hand


class StraightFlush:
    def __init__(self, card: Card):
        self.card = card

    def __lt__(self, other):
        return self.card.number < other.card.number

    def __eq__(self, other):
        return self.card == other.card


def straight_flush_of(hand: Hand, board: List[Card]):
    if flush_of(hand, board) is None or straight_of(hand, board) is None:
        return None
    else:
        cards = [card for card in hand] + board.cards
        for card in cards:
            if all(card.decrease(i) in cards for i in range(1, 5)):
                return StraightFlush(card)
        else:
            return None
