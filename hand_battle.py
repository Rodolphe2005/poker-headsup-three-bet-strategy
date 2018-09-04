from permutations import permutations_of


def hand_battle(two_hands, d):
    hand1, hand2 = two_hands.split('-')
    for s1, s2, s3, s4 in permutations_of([hand1[1], hand1[3], hand2[1], hand2[3]]):
        y = hand1[0] + s1 + hand1[2] + s2 + '-' + hand2[0] + s3 + hand2[2] + s4
        if y in d:
            print('using ' + y)
            return d[y]
    return None