from hand_battle.card import Card
from hand_battle.hand import Hand


def test_hand_initialization():
    hand = Hand('QhJs')
    assert hand.card1 == Card('Qh')
    assert hand.card2 == Card('Js')


def test_hand_comparison():
    assert Hand('QhJs') == Hand('JsQh')
    assert Hand('QhJs') != Hand('QsJs')
