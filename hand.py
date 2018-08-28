from card import Card


class Hand:
    def __init__(self, name):
        self.card1 = Card(name[:2])
        self.card2 = Card(name[2:])

    def __eq__(self, other):
        return {self.card1, self.card2} == {other.card1, other.card2}
