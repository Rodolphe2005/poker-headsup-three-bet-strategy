from board import Board
from card import Card
from hand import Hand
from showdown_strengths.flush import Flush, flush_of

q_high_flush_cards = [Card(name + 'h') for name in ['Q', 'T', '9', '8', '7']]
j_high_flush_cards = [Card(name + 'h') for name in ['J', 'T', '9', '8', '7']]


def flush_initialization():
    assert Flush(q_high_flush_cards).cards == q_high_flush_cards


def test_flush_comparison():
    assert Flush(q_high_flush_cards) == Flush(q_high_flush_cards)
    assert Flush(j_high_flush_cards) < Flush(q_high_flush_cards)


def test_flush_of():
    expected = Flush([Card(name + 'h') for name in 'QJT98'])
    actual = flush_of(Hand('QhJs'), Board('JhTh9h8h2d'))
    assert expected == actual
