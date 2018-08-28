from card import suits, Card
from card_number import card_number_names
from random import sample


class Deck:
    def __init__(self):
        self.cards = {Card(number + suit)
                      for number in card_number_names
                      for suit in suits}

    def __iter__(self):
        for card in self.cards:
            yield card

    def __contains__(self, item):
        return item in self.cards

    def remove(self, card):
        self.cards.remove(card)

    def random_board(self):
        return sample(self.cards, 5)
