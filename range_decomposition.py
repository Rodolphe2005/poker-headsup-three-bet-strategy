from permutations import suits


def range_decomposition(hand):
    if len(hand) == 2 and hand[0] == hand[1]:
        yield from pair_decomposition(hand)
    else:
        c1, c2, suited_marker = hand
        assert c1 != c2
        if suited_marker == 's':
            yield from suited_decomposition(hand)
        elif suited_marker == 'o':
            yield from offsuit_decomposition(hand)
        else:
            raise Exception


def pair_decomposition(hand):
    assert len(hand) == 2 and hand[0] == hand[1]
    for s1 in suits:
        for s2 in suits:
            if hand[0] == hand[1]:
                if s1 == s2:
                    continue
            yield hand[0] + s1 + hand[1] + s2


def suited_decomposition(hand):
    c1, c2, suited_marker = hand
    assert suited_marker == 's' and c1 != c2
    for s in suits:
        yield c1 + s + c2 + s


def offsuit_decomposition(hand):
    c1, c2, suited_marker = hand
    assert suited_marker == 'o' and c1 != c2
    for s1 in suits:
        for s2 in suits:
            if s1 == s2:
                continue
            yield c1 + s1 + c2 + s2
