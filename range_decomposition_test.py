from range_decomposition import range_decomposition


def test_pair_decomposition():
    hands = range_decomposition('JJ')
    assert len(set(hands)) == 12


def test_suited_decomposition():
    hands = range_decomposition('T9s')
    assert len(set(hands)) == 4


def test_offsuit_decomposition():
    hands = range_decomposition('T9o')
    assert len(set(hands)) == 12
