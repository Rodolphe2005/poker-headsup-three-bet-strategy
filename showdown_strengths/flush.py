from board import Board
from card import Card, suits
from hand import Hand


class Flush:
    ranking = 6

    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        cards_names = ''.join([card.name for card in self.cards])
        return f'Flush({cards_names})'

    def __eq__(self, other):
        return all(card1.number == card2.number
                   for card1, card2 in zip(self.cards, other.cards))

    def __lt__(self, other):
        for card1, card2 in zip(self.cards, other.cards):
            if card1.number > card2.number:
                return False
        return True


def flush_of(hand: Hand, board: Board):
    cards = [hand.card1, hand.card2] + board.cards
    for suit in suits:
        cards_of_this_suit = [card for card in cards if card.suit == suit]
        if len(cards_of_this_suit) >= 5:
            sorted_card_numbers = sorted([card.number for card in cards_of_this_suit], reverse=True)
            return Flush([Card(number.name + suit) for number in sorted_card_numbers])
