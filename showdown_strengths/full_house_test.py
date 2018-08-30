from board import Board
from card_number import CardNumber
from hand import Hand
from showdown_strengths.full_house import FullHouse, full_house_of


def test_full_house_initialization():
    full_house = FullHouse(CardNumber('Q'), CardNumber('J'))
    assert full_house.trips == CardNumber('Q')
    assert full_house.pair == CardNumber('J')


def test_full_house_comparison():
    assert FullHouse(CardNumber('Q'), CardNumber('J')) < FullHouse(CardNumber('K'), CardNumber('J'))
    assert FullHouse(CardNumber('Q'), CardNumber('J')) < FullHouse(CardNumber('Q'), CardNumber('A'))
    assert FullHouse(CardNumber('Q'), CardNumber('J')) == FullHouse(CardNumber('Q'), CardNumber('J'))


def test_full_house_of():
    expected = FullHouse(CardNumber('Q'), CardNumber('T'))
    actual = full_house_of(Hand('QhQs'), Board('QcThTc9h8s'))
    assert expected == actual
