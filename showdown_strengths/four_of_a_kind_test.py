from board import Board
from hand import Hand
from showdown_strengths.four_of_a_kind import FourOfAKind, four_of_a_kind_of


def test_four_of_a_kind_initialization():
    assert FourOfAKind('Q').kicker.name == 'Q'


def test_four_of_a_kind_comparison():
    assert FourOfAKind('Q') < FourOfAKind('K')


def test_four_of_a_kind_of():
    expected = FourOfAKind('Q')
    actual = four_of_a_kind_of(Hand('QhJs'), Board('JhJdJc8h2d'))
    assert expected == actual

    expected = None
    actual = four_of_a_kind_of(Hand('QhJs'), Board('JhTdJc8h2d'))
    assert expected == actual
