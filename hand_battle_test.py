from hand_battle import hand_battle


def test_hand_battle():
    x = hand_battle('JsJd-KhKc', d={'JdJc-KsKh': 0.6})
    assert x == 0.6

    x = hand_battle('JsJh-KhKc', d={'JdJc-KsKh': 0.6})
    assert x is None