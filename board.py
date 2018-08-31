from card import Card


class Board:
    def __init__(self, name):
        self.cards = [Card(name[i: i+2]) for i in range(0, 10, 2)]

    def __repr__(self):
        return f'Board({self.cards_to_name(self.cards)})'

    @staticmethod
    def cards_to_name(cards):
        return ''.join([card.name for card in cards])
