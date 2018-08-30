from collections import Counter

from board import Board
from card_number import CardNumber
from hand import Hand


class ThreeOfAKind:
    def __init__(self, number, kicker1, kicker2):
        self.number = CardNumber(number)
        self.kicker1 = CardNumber(kicker1)
        self.kicker2 = CardNumber(kicker2)

    def __repr__(self):
        return f'ThreeOfAKind({self.number.name}, {self.kicker1.name}, {self.kicker2.name})'

    def __eq__(self, other):
        return self.number == other.number and self.kicker1 == other.kicker1 and self.kicker2 == other.kicker2

    def __lt__(self, other):
        if self.number != other.number:
            return self.number < other.number

        if self.kicker1 != other.kicker1:
            return self.kicker1 < other.kicker1

        if self.kicker2 != other.kicker2:
            return self.kicker2 < other.kicker2


def three_of_a_kind_of(hand: Hand, board: Board):
    cards = hand.cards + board.cards
    cards_numbers = [card.number for card in cards]
    counter = Counter(cards_numbers)
    counter_of_occurences = Counter(counter.values())
    if counter_of_occurences == {3: 1, 1: 4}:
        trips_number = max(card_number
                           for card_number, count in counter.items()
                           if count == 3)
        possible_kickers = sorted([
            card_number for card_number, count in counter.items() if count == 1
        ], reverse=True)
        kicker1 = possible_kickers[0]
        kicker2 = possible_kickers[1]
        return ThreeOfAKind(trips_number.name, kicker1.name, kicker2.name)
