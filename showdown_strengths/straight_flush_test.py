from board import Board
from hand import Hand
from showdown_strengths.straight_flush import StraightFlush, straight_flush_of


def straight_flush_initialization():
    assert StraightFlush('Qh').card.name == 'Qh'


def test_straight_flush_comparison():
    assert StraightFlush('Qh') == StraightFlush('Qh')
    assert StraightFlush('Jh') < StraightFlush('Qh')


def test_straight_flush_of():
    expected = StraightFlush('Qh')
    actual = straight_flush_of(Hand('QhJs'), Board('JhTh9h8h2d'))
    assert expected == actual
