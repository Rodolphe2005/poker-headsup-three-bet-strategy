from card import Card


class Board:
    def __init__(self, name):
        self.cards = [Card(name[i: i+2]) for i in range(0, 10, 2)]