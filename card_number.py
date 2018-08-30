card_number_names = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

class CardNumber:
    def __init__(self, name):
        self.name = name
        self.value = card_number_names.index(name) + 2

    def __repr__(self):
        return f'CardNumber({str(self.value)})'

    def __hash__(self):
        return self.name.__hash__()

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.name == other.name

    def decrease(self, i):
        value = self.value - i
        index = value - 2
        if index<0:
            return None
        else:
            return CardNumber(card_number_names[index])