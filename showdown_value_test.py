from board import Board
from hand import Hand
from showdown_strengths.flush import Flush
from showdown_strengths.four_of_a_kind import FourOfAKind
from showdown_strengths.full_house import FullHouse
from showdown_strengths.high_card import HighCard
from showdown_strengths.pair import Pair
from showdown_strengths.straight import Straight
from showdown_strengths.straight_flush import StraightFlush
from showdown_strengths.three_of_a_kind import ThreeOfAKind
from showdown_strengths.two_pair import TwoPair
from showdown_value import showdown_value_of


def test_straight_flush():
    expected = StraightFlush('Qh')
    actual = showdown_value_of(Hand('QhJh'), Board('Th9h8h2d2c'))
    assert expected == actual


def test_four_of_a_kind():
    expected = FourOfAKind('J')
    actual = showdown_value_of(Hand('QhJh'), Board('QcQsQd2h3h'))
    assert expected == actual


def test_full_house():
    expected = FullHouse('J', 'T')
    actual = showdown_value_of(Hand('JhTs'), Board('JsJcTh2h3h'))
    assert expected == actual


def test_flush():
    expected = Flush(['Jh', 'Th', '6h', '5h', '4h'])
    actual = showdown_value_of(Hand('Jh4h'), Board('Th6h5h2dAd'))
    assert expected == actual


def test_straight():
    expected = Straight('J')
    actual = showdown_value_of(Hand('Jh2s'), Board('Td9c8h7s3d'))
    assert expected == actual


def test_three_of_a_kind():
    expected = ThreeOfAKind('J', '8', '7')
    actual = showdown_value_of(Hand('JsJh'), Board('Jc8s7h3d2d'))
    assert expected == actual


def test_two_pair():
    expected = TwoPair('J', '8', '7')
    actual = showdown_value_of(Hand('JsJh'), Board('8c8s7h3d2d'))
    assert expected == actual


def test_pair():
    expected = Pair('J', '8', '7', '6')
    actual = showdown_value_of(Hand('JsJh'), Board('8s7h6d3d2d'))
    assert expected == actual


def test_high_card():
    expected = HighCard('J', '8', '7', '5', '4')
    actual = showdown_value_of(Hand('Js8h'), Board('7h5h4d3d2d'))
    assert expected == actual
