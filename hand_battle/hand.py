from hand_battle.card import Card


class Hand:
    def __init__(self, name):
        self.card1 = Card(name[:2])
        self.card2 = Card(name[2:])

    def __repr__(self):
        return f'Hand({self.card1.name}{self.card2.name})'

    def __eq__(self, other):
        return {self.card1, self.card2} == {other.card1, other.card2}

    @property
    def cards(self):
        return [self.card1, self.card2]