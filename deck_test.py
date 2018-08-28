from card import Card
from deck import Deck


def test_deck_initialization():
    deck = Deck()
    assert len(deck.cards) == 52


def test_card_removal():
    deck = Deck()
    deck.remove(Card('Qh'))
    assert len(deck.cards) == 51
    for card in deck:
        assert card != Card('Qh')
    assert Card('As') in deck


def test_random_board():
    deck = Deck()
    random_board = deck.random_board()
    assert len(random_board) == 5
    assert isinstance(random_board[0], Card)
