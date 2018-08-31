from board import Board
from card_number import CardNumber
from hand import Hand
from showdown_strengths.straight import Straight, straight_of


def flush_initialization():
    assert Straight('Q').card_number == CardNumber('Q')


def test_straight_comparison():
    assert Straight('Q') == Straight('Q')
    assert Straight('J') < Straight('Q')


def test_straight_of():
    expected = Straight('Q')
    actual = straight_of(Hand('QhJs'), Board('JhTh9h8h2d'))
    assert expected == actual
