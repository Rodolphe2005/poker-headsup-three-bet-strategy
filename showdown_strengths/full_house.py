from collections import Counter

from board import Board
from card_number import CardNumber
from hand import Hand


class FullHouse:
    ranking = 7

    def __init__(self, trips: CardNumber, pair: CardNumber):
        self.trips = trips
        self.pair = pair

    def __repr__(self):
        return f'FullHouse({self.trips.name}, {self.pair.name})'

    def __eq__(self, other):
        return self.trips == other.trips and self.pair == other.pair

    def __lt__(self, other):
        return self.trips < other.trips or (self.trips == other.trips and self.pair < other.pair)


def full_house_of(hand: Hand, board: Board):
    cards = hand.cards + board.cards
    counter = Counter([card.number for card in cards])
    if 2 in counter.values() and 3 in counter.values():
        possible_trips = [card_number for card_number, count in counter.items() if count == 3]
        possible_pairs = [card_number for card_number, count in counter.items() if count == 2]
        assert len(possible_trips) == 1
        assert 1 <= len(possible_pairs) <= 2
        return FullHouse(max(possible_trips), max(possible_pairs))