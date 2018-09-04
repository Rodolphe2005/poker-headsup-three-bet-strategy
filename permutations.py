from itertools import permutations

suits = ['h', 'c', 's', 'd']


def all_permutations():
    for y1 in suits:
        for y2 in suits:
            if y2 == y1:
                continue
            for y3 in suits:
                if y3 in {y1, y2}:
                    continue
                for y4 in suits:
                    if y4 in {y1, y2, y3}:
                        continue
                    yield dict(zip(suits, [y1, y2, y3, y4]))


def permutations_of(x):
    return {tuple(p[i] for i in x) for p in all_permutations()}
