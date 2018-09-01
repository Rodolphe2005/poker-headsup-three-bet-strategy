from hand_battle.hand import Hand
from hand_battle import equity_of
from showdown_strengths.flush import flush_of
from showdown_strengths.four_of_a_kind import four_of_a_kind_of
from showdown_strengths.full_house import full_house_of
from showdown_strengths.high_card import high_card_of
from showdown_strengths.pair import pair_of
from showdown_strengths.straight import straight_of
from showdown_strengths.straight_flush import straight_flush_of
from showdown_strengths.three_of_a_kind import three_of_a_kind_of
from showdown_strengths.two_pair import two_pair_of
from hand_battle.showdown_value import showdown_value_of
from utils import do_profile


@do_profile(follow=[
    equity_of,
    showdown_value_of,
    straight_flush_of,
    four_of_a_kind_of,
    full_house_of,
    flush_of,
    straight_of,
    three_of_a_kind_of,
    two_pair_of,
    pair_of,
    high_card_of
])
def test_pair_versus_pair():
    equity = equity_of(Hand('ThTs'), Hand('AcAd'), iterations=10**7)
    assert 0.18 < equity < 0.22

test_pair_versus_pair()