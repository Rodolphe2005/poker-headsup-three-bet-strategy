from showdown_strengths.flush import Flush
from showdown_strengths.four_of_a_kind import FourOfAKind
from showdown_strengths.full_house import FullHouse
from showdown_strengths.straight_flush import StraightFlush
from showdown_strengths.straight import Straight

showdown_strengths = [
    StraightFlush,
    FourOfAKind,
    FullHouse,
    Flush,
    Straight,
    ThreeOfAKind,
    # TwoPair,
    # Pair,
    # HighCard
]


def test_showdown_strengths_orders():
    for i, strength1 in enumerate(showdown_strengths):
        for strength2 in showdown_strengths[i + 1:]:
            assert strength1.ranking > strength2.ranking