from board import Board
from card_number import CardNumber
from hand import Hand


class Straight:
    def __init__(self, card_number: CardNumber):
        self.card_number = card_number

    def __eq__(self, other):
        return self.card_number == other.card_number

    def __lt__(self, other):
        return self.card_number < other.card_number


def straight_of(hand: Hand, board: Board):
    cards = [hand.card1, hand.card2] + board.cards
    card_numbers = [card.number for card in cards]
    for card_number in card_numbers:
        if all(card_number.decrease(i) in card_numbers for i in range(1, 5)):
            return Straight(card_number)
    else:
        return None
