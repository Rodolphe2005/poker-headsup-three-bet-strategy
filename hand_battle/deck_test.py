from hand_battle.board import Board
from hand_battle.card import Card
from hand_battle.deck import Deck


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
    assert isinstance(random_board, Board)
