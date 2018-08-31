from board import Board
from hand import Hand
from showdown_strengths.pair import Pair, pair_of


def test_pair_initialization():
    pair = Pair('Q', 'A', 'K', '8')
    assert pair.pair.name == 'Q'
    assert pair.kicker1.name == 'A'
    assert pair.kicker2.name == 'K'
    assert pair.kicker3.name == '8'


def test_pair_comparison():
    assert Pair('J', 'A', 'K', '8') < Pair('Q', 'A', 'K', '8')
    assert Pair('J', 'K', 'T', '8') < Pair('J', 'K', 'Q', '8')
    assert Pair('J', 'A', 'K', '8') == Pair('J', 'A', 'K', '8')


def test_pair_of():
    expected = Pair('Q', 'T', '9', '8')
    actual = pair_of(Hand('Qh2s'), Board('QcTh9h8s6h'))
    assert expected == actual
