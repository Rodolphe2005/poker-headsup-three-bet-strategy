from hand import Hand
from three_bet_strategy.call_equity import call_equity, three_bet_equity


def test_call_equity():
    for s in range(5, 100, 5):
        call_value = call_equity(Hand(name='54o', combos=16), steal=s)
        assert call_value < 0

        three_bet_value = three_bet_equity(
            Hand(name='54o', combos=16),
            steal=s,
            fold_percentage=100)
        assert three_bet_value == 2.5
