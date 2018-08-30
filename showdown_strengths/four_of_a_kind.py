from collections import Counter

from board import Board
from card_number import CardNumber
from hand import Hand


class FourOfAKind:
    ranking = 8

    def __init__(self, kicker: str):
        self.kicker = CardNumber(kicker)

    def __repr__(self):
        return f'FourOfAKind({self.kicker.name})'

    def __eq__(self, other):
        return self.kicker == other.kicker

    def __lt__(self, other):
        return self.kicker < other.kicker

def four_of_a_kind_of(hand: Hand, board: Board):
    cards = hand.cards + board.cards
    card_numbers = [card.number for card in cards]
    for card_number, count in Counter(card_numbers).items():
        if count == 4:
            possible_kickers = [card.number.name for card in cards if card.number!=card_number]
            return FourOfAKind(max(possible_kickers))