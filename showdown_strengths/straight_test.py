from board import Board
from card import Card
from card_number import CardNumber
from hand import Hand
from showdown_strengths.flush import Flush, flush_of
from showdown_strengths.straight import Straight, straight_of


def flush_initialization():
    assert Straight(CardNumber('Q')).card_number == CardNumber('Q')


def test_straight_comparison():
    assert Straight(CardNumber('Q')) == Straight(CardNumber('Q'))
    assert Straight(CardNumber('J')) < Straight(CardNumber('Q'))


def test_straight_of():
    expected = Straight(CardNumber('Q'))
    actual = straight_of(Hand('QhJs'), Board('JhTh9h8h2d'))
    assert expected == actual
