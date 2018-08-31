from deck import Deck
from hand import Hand
from showdown_value import showdown_value_of


def equity_of(hand1: Hand, hand2: Hand):
    counts = {1: 0, 2: 0}
    for i in range(1000000):
        deck = Deck()
        deck.remove(hand1.card1)
        deck.remove(hand1.card2)
        deck.remove(hand2.card1)
        deck.remove(hand2.card2)
        board = deck.random_board()
        value1 = showdown_value_of(hand1, board)
        value2 = showdown_value_of(hand2, board)
        if value1.ranking < value2.ranking:
            counts[2] += 1
        elif value1.ranking > value2.ranking:
            counts[1] += 1
        else:
            if value1 < value2:
                counts[2] += 1
            elif value1 > value2:
                counts[1] += 1
            else:
                counts[2] += 0.5
                counts[1] += 0.5

        if i % 10000 == 0:
            print(counts[1] / (counts[1]+counts[2]))

    return counts[1] / (counts[1]+counts[2])
