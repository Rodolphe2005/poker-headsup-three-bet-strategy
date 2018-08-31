from collections import Counter

from board import Board
from card_number import CardNumber
from hand import Hand


class FullHouse:
    ranking = 7

    def __init__(self, trips: str, pair: str):
        self.trips = CardNumber(trips)
        self.pair = CardNumber(pair)

    def __repr__(self):
        return f'FullHouse({self.trips.name}, {self.pair.name})'

    def __eq__(self, other):
        return self.trips == other.trips and self.pair == other.pair

    def __lt__(self, other):
        return self.trips < other.trips or (self.trips == other.trips and self.pair < other.pair)


def full_house_of(hand: Hand, board: Board):
    cards = hand.cards + board.cards
    counter = Counter([card.number for card in cards])
    if 3 in counter.values():
        possible_trips = [card_number.name for card_number, count in counter.items() if count == 3]
        trips_card_name = max(possible_trips)
        counter2 = Counter([card.number for card in cards if card.name != trips_card_name])
        if 2 in counter2.values() or 3 in counter2.values():
            possible_pairs = [card_number.name for card_number, count in counter2.items() if count == 2 or count==3]
            pair_card_name = max(possible_pairs)
            return FullHouse(trips_card_name, pair_card_name)