from permutations import suits


def range_decomposition(hand):
    for s1 in suits:
        for s2 in suits:
            if hand[0] == hand[1]:
                if s1 == s2:
                    continue
            yield hand[0] + s1 + hand[1] + s2


def test_range_decomposition():
    hands = range_decomposition('JJ')
    assert len(list(hands)) == 12
