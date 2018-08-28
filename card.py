from card_number import CardNumber

suits = ['h', 's', 'd', 'c']


class Card:
    def __init__(self, card_name: str):
        self.number = CardNumber(card_name[:-1])
        self.suit = card_name[-1]

    def __hash__(self):
        return (self.number.name + self.suit).__hash__()

    def __repr__(self):
        return f'Card({self.number.name + self.suit})'

    def __eq__(self, other):
        return self.number == other.number and self.suit == other.suit

    def decrease(self, i):
        new_number = self.number.decrease(i)
        return Card(new_number.name + self.suit)

    @property
    def name(self):
        return self.number.name + self.suit