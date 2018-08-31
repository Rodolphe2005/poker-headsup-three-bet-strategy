from board import Board
from hand import Hand
from showdown_strengths.two_pair import TwoPair, two_pair_of


def test_two_pair_initialization():
    two_pair = TwoPair('A', 'Q', 'K')
    assert two_pair.pair1.name == 'A'
    assert two_pair.pair2.name == 'Q'
    assert two_pair.kicker.name == 'K'


def test_two_pair_comparison():
    assert TwoPair('A', 'J', 'K') < TwoPair('A', 'Q', 'K')
    assert TwoPair('A', 'J', 'T') < TwoPair('A', 'J', 'Q')
    assert TwoPair('A', 'J', 'K') == TwoPair('A', 'J', 'K')


def test_two_pair_of():
    expected = TwoPair('Q', 'T', '9')
    actual = two_pair_of(Hand('QhQs'), Board('ThTd9h8s6h'))
    assert expected == actual
