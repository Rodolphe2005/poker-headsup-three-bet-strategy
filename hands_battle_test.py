from hand import Hand
from hand_battle import equity_of


def test_pair_versus_pair():
    equity = equity_of(Hand('ThTs'), Hand('AcAd'))
    assert 0.18 < equity < 0.22

test_pair_versus_pair()