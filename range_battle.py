import os
from collections import defaultdict
from json import JSONDecodeError
from numpy import nan

from flask import json


def load_hand_battle_computed():
    hand_battles = defaultdict(dict)
    dirname = os.path.dirname(__file__)
    for filename in os.listdir(dirname + '/hands/'):
        if not filename.endswith('.json'):
            continue
        try:
            with open(dirname + '/hands/' + filename, 'r') as fp:
                hand_results = json.load(fp)
                for range_battle_name, result in hand_results.items():
                    hand1, hand2 = range_battle_name.split('-')
                    hand_battles[hand1][hand2] = result
        except JSONDecodeError:
            print('Problem with ' + filename)
    return hand_battles


hand_battles = load_hand_battle_computed()


def range_battle(range1, range2):
    if len(range2) == 0:
        return nan
    return sum([
        hand_battles[hand1.name][hand2.name] * hand1.combos * hand2.combos
        for hand1 in range1
        for hand2 in range2
    ]) / sum([
        hand1.combos * hand2.combos
        for hand1 in range1
        for hand2 in range2
    ])
