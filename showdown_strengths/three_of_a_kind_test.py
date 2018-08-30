from board import Board
from hand import Hand
from showdown_strengths.three_of_a_kind import ThreeOfAKind, three_of_a_kind_of


def test_three_of_a_kind_initialization():
    three_of_a_kind = ThreeOfAKind('Q', 'A', 'K')
    assert three_of_a_kind.number.name == 'Q'
    assert three_of_a_kind.kicker1.name == 'A'
    assert three_of_a_kind.kicker2.name == 'K'


def test_three_of_a_kind_comparison():
    assert ThreeOfAKind('J', 'A', 'K') < ThreeOfAKind('Q', 'A', 'K')
    assert ThreeOfAKind('J', 'K', 'T') < ThreeOfAKind('J', 'K', 'Q')
    assert ThreeOfAKind('J', 'A', 'K') == ThreeOfAKind('J', 'A', 'K')


def test_full_house_of():
    expected = ThreeOfAKind('Q', 'T', '9')
    actual = three_of_a_kind_of(Hand('QhQs'), Board('QcTh9h8s6h'))
    assert expected == actual
