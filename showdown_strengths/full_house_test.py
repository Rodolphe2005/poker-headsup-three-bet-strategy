from board import Board
from card_number import CardNumber
from hand import Hand
from showdown_strengths.full_house import FullHouse, full_house_of


def test_full_house_initialization():
    full_house = FullHouse('Q', 'J')
    assert full_house.trips.name == 'Q'
    assert full_house.pair.name == 'J'


def test_full_house_comparison():
    assert FullHouse('Q', 'J') < FullHouse('K', 'J')
    assert FullHouse('Q', 'J') < FullHouse('Q', 'A')
    assert FullHouse('Q', 'J') == FullHouse('Q', 'J')


def test_full_house_of():
    expected = FullHouse('Q', 'T')
    actual = full_house_of(Hand('QhQs'), Board('QcThTc9h8s'))
    assert expected == actual
