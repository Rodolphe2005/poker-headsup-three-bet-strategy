from hand import Hand
from range_battle import range_battle


def test_range_battle():
    assert range_battle([Hand(name='54o', combos=1)], [Hand(name='55', combos=1)]) < 0.2

    assert range_battle(
        [Hand('54o', combos=1)],
        [Hand('55', combos=1), Hand('22', combos=1), Hand('32o', combos=1)]
    ) > 0.2

    assert range_battle(
        [Hand('54o', combos=1)],
        [Hand('55', combos=10000), Hand('22', combos=1), Hand('32o', combos=1)]
    ) < 0.2
