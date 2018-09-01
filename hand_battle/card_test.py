from hand_battle.card import Card, suits
from hand_battle.card_number import card_number_names


def test_card_initialization():
    card = Card('Qh')
    assert card.number.value == 12
    assert card.suit == 'h'


def test_card_order():
    for suit1 in suits:
        for suit2 in suits:
            for i, value1 in enumerate(card_number_names):
                for value2 in card_number_names[i + 1:]:
                    assert Card(value1 + suit1).number == Card(value1 + suit2).number
                    assert Card(value1 + suit1).number < Card(value2 + suit2).number
