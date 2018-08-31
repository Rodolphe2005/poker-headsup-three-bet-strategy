from board import Board
from hand import Hand
from showdown_strengths.high_card import HighCard, high_card_of


def test_high_card_initialization():
    high_card = HighCard('A', 'K', 'Q', '8', '6')
    assert high_card.high_card.name == 'A'
    assert high_card.kicker1.name == 'K'
    assert high_card.kicker2.name == 'Q'
    assert high_card.kicker3.name == '8'
    assert high_card.kicker4.name == '6'


def test_high_card_comparison():
    assert HighCard('A', 'K', 'J', '8', '6') < HighCard('A', 'K', 'Q', '8', '6')
    assert HighCard('K', 'J', 'T', '8', '6') < HighCard('K', 'Q', 'T', '8', '6')
    assert HighCard('A', 'K', 'J', '8', '6') == HighCard('A', 'K', 'J', '8', '6')


def test_high_card_of():
    expected = HighCard('Q', 'T', '9', '8', '6')
    actual = high_card_of(Hand('Qh3s'), Board('2cTh9h8s6h'))
    assert expected == actual
