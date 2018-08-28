from showdown_strengths.straight_flush import StraightFlush

showdown_strengths = [
    StraightFlush,
    FourOfAKind,
    FullHouse,
    Flush,
    Straigth,
    ThreeOfAKind,
    TwoPair,
    Pair,
    HighCard
]

def test_showdown_strengths_orders():
    for i, strength1 in enumerate(showdown_strengths):
        for strength2 in showdown_strengths[i+1:]:
            assert strength1 > strength2