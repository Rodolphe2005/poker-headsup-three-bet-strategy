from collections import Counter

from board import Board
from card_number import CardNumber
from hand import Hand


class TwoPair:
    ranking = 3

    def __init__(self, pair1, pair2, kicker):
        self.pair1 = CardNumber(pair1)
        self.pair2 = CardNumber(pair2)
        self.kicker = CardNumber(kicker)

    def __repr__(self):
        return f'TwoPair({self.pair1.name}, {self.pair2.name}, {self.kicker.name})'

    def __eq__(self, other):
        return self.pair1 == other.pair1 and self.pair2 == other.pair2 and self.kicker == other.kicker

    def __lt__(self, other):
        if self.pair1 != other.pair1:
            return self.pair1 < other.pair1

        if self.pair2 != other.pair2:
            return self.pair2 < other.pair2

        if self.kicker != other.kicker:
            return self.kicker < other.kicker


def two_pair_of(hand: Hand, board: Board):
    cards = hand.cards + board.cards
    cards_numbers = [card.number for card in cards]
    counter = Counter(cards_numbers)
    counter_of_occurrences = Counter(counter.values())
    if counter_of_occurrences == {2: 2, 1: 3} or counter_of_occurrences == {2: 3, 1: 1}:
        pairs = [card_number
                 for card_number, count in counter.items()
                 if count == 2]
        possible_kickers = sorted([
            card_number
            for card_number, count in counter.items()
            if count == 1
        ], reverse=True)

        return TwoPair(max(pairs).name, min(pairs).name, max(possible_kickers).name)
