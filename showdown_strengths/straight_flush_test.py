from card import Card
from showdown_strengths.straight_flush import StraightFlush


def straight_flush_initialization():
    assert StraightFlush(Card('Qh')).card == Card('Qh')


def test_straight_flush_comparison():
    assert StraightFlush(Card('Qh')) == StraightFlush(Card('Qh'))
    assert StraightFlush(Card('Jh')) < StraightFlush(Card('Qh'))
