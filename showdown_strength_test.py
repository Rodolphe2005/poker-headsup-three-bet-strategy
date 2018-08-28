from showdown_strengths.flush import Flush
from showdown_strengths.straight_flush import StraightFlush
from showdown_strengths.straight import Straight

showdown_strengths = [
    StraightFlush,
    #FourOfAKind,
    #FullHouse,
    Flush,
    Straight,
    #ThreeOfAKind,
    #TwoPair,
    #Pair,
    #HighCard
]

def test_showdown_strengths_orders():
    for i, strength1 in enumerate(showdown_strengths):
        for strength2 in showdown_strengths[i+1:]:
            assert strength1 > strength2