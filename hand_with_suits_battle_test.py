from hand_with_suits_battle import hand_with_suits_battle


def test_hand_battle():
    x = hand_with_suits_battle('JsJd-KhKc', d={'JdJc-KsKh': 0.6})
    assert x == 0.6

    x = hand_with_suits_battle('JsJh-KhKc', d={'JdJc-KsKh': 0.6})
    assert x is None