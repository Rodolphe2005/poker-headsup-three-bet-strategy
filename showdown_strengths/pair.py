from collections import Counter

from board import Board
from card_number import CardNumber
from hand import Hand


class Pair:
    ranking = 2

    def __init__(self, pair, kicker1, kicker2, kicker3, kicker4):
        self.pair = CardNumber(pair)
        self.kicker1 = CardNumber(kicker1)
        self.kicker2 = CardNumber(kicker2)
        self.kicker3 = CardNumber(kicker3)
        self.kicker4 = CardNumber(kicker4)

    def __repr__(self):
        return f'Pair({self.pair}, {self.kicker1}, {self.kicker2}, ' \
               f'{self.kicker3}, {self.kicker4})'

    def __eq__(self, other):
        return self.as_array() == other.as_array()

    def __lt__(self, other):
        return self.as_array() < other.as_array()

    def as_array(self):
        return [self.pair, self.kicker1, self.kicker2, self.kicker3, self.kicker4]


def pair_of(hand: Hand, board: Board):
    cards = hand.cards + board.cards
    cards_numbers = [card.number for card in cards]
    counter = Counter(cards_numbers)
    counter_of_occurrences = Counter(counter.values())
    if counter_of_occurrences == {2: 1, 1: 5}:
        pairs = [card_number
                 for card_number, count in counter.items()
                 if count == 2]
        possible_kickers = sorted([
            card_number
            for card_number, count in counter.items()
            if count == 1
        ], reverse=True)

        return Pair(max(pairs).name,
                    possible_kickers[0].name,
                    possible_kickers[1].name,
                    possible_kickers[2].name,
                    possible_kickers[3].name,
                    )
