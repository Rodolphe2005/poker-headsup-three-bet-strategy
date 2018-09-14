import os
import json
from collections import defaultdict, namedtuple
from json import JSONDecodeError
from pprint import pprint

import numpy as np

from hand import Hand


def combos_of(hand_name):
    if len(hand_name) == 2:
        return 6
    else:
        assert len(hand_name) == 3
        if hand_name[-1] == 'o':
            return 12
        elif hand_name[-1] == 's':
            return 4
        else:
            raise ValueError


def compute_hands_strengths():
    hand_value = defaultdict(list)
    dirname = os.path.dirname(__file__)
    for filename in os.listdir(dirname + '/hands/'):
        if not filename.endswith('.json'):
            continue
        try:
            with open(dirname + '/hands/' + filename, 'r') as fp:
                hand_results = json.load(fp)
                for range_battle_name, result in hand_results.items():
                    hand1, hand2 = range_battle_name.split('-')
                    hand_value[hand2].append(1 - result)
        except JSONDecodeError:
            print('Problem with ' + filename)


    hands = [
        Hand(
            name=name,
            strength=np.round(np.mean(local_strengths), 3),
            combos=combos_of(name),
            frequency=combos_of(name) / (52 * 51 / 2) * 100
        )
        for name, local_strengths in hand_value.items()
    ]
    return hands


hands_strengths = compute_hands_strengths()
sorted_hands_strengths = sorted(hands_strengths, key=lambda x: x.strength, reverse=True)
pprint(sorted_hands_strengths)

def get_top_x_percent_of_hands(x):
    """x between 0 and 100"""
    current_frequency = 0
    for hand in sorted_hands_strengths:
        if current_frequency + hand.frequency > x:
            break
        current_frequency += hand.frequency
        yield hand
