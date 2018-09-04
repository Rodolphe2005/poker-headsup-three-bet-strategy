from permutations import permutations_of, all_permutations


def test_all_permutations():
    assert len(list(all_permutations())) == 24


def test_permutations_lengths():
    for x, n in [
        (['c', 'd', 'h', 's'], 4 * 3 * 2),
        (['c', 'c', 'h', 's'], 4 * 3 * 2),
        (['c', 'c', 'c', 's'], 4 * 3),
        (['c', 'c', 'c', 'c'], 4),
    ]:
        assert len(permutations_of(x)) == n


def test_permutations_values():
    assert ('d', 'd', 'c', 's') in permutations_of(['c', 'c', 'h', 's'])
    assert ('d', 'd', 'd', 's') in permutations_of(['c', 'c', 'c', 'd'])
    assert ('d', 'd', 'd', 'd') in permutations_of(['c', 'c', 'c', 'c'])
