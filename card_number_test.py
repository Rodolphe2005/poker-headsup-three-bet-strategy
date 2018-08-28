from card_number import card_number_names, CardNumber


def test_card_number_initialization():
    for i, name in enumerate(card_number_names):
        card_number = CardNumber(name)
        assert i + 2 == card_number.value


def test_decrease():
    assert CardNumber('Q').decrease(0) == CardNumber('Q')
    assert CardNumber('Q').decrease(2) == CardNumber('T')
    assert CardNumber('Q').decrease(20) is None
