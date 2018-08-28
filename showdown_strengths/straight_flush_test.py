from board import Board
from card import Card
from hand import Hand
from showdown_strengths.straight_flush import StraightFlush, straight_flush_of


def straight_flush_initialization():
    assert StraightFlush(Card('Qh')).card == Card('Qh')


def test_straight_flush_comparison():
    assert StraightFlush(Card('Qh')) == StraightFlush(Card('Qh'))
    assert StraightFlush(Card('Jh')) < StraightFlush(Card('Qh'))


def test_straight_flush_of():
    expected = StraightFlush(Card('Qh'))
    actual = straight_flush_of(Hand('QhJs'), Board('JhTh9h8h2d'))
    assert expected == actual
