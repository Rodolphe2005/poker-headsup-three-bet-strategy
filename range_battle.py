from flask import json
import os

from hand_battle import hand_battle
from pokerlistings_calls import query
from range_decomposition import range_decomposition
import numpy as np

possible_cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
possible_suits = ['', 'o', 's']


def range_battle(two_ranges):
    d = {}
    range1, range2 = two_ranges.split('-')
    for hand1 in range_decomposition(range1):
        for hand2 in range_decomposition(range2):
            result = hand_battle(hand1 + '-' + hand2, d)
            if result is None:
                card1 = hand1[:2]
                card2 = hand1[2:4]
                card3 = hand2[:2]
                card4 = hand2[2:4]

                if len({card1, card2, card3, card4}) != 4:
                    continue
                result = query(card1, card2, card3, card4)
            d[hand1 + '-' + hand2] = result
    return d


def possible_hands():
    for i, card1 in enumerate(possible_cards):
        for card2 in possible_cards[:i + 1]:
            for possible_suit1 in possible_suits:
                if card1 == card2 and possible_suit1 != '':
                    continue
                if card1 != card2 and possible_suit1 == '':
                    continue
                yield card1, card2, possible_suit1


for card1, card2, possible_suit1 in possible_hands():
    hand1 = card1 + card2 + possible_suit1
    file_path = 'hands/' + hand1 + '.json'
    if os.path.isfile(file_path):
        continue

    hand_results = {}
    for card3, card4, possible_suit2 in possible_hands():
        hand2 = card3 + card4 + possible_suit2
        battle_name = hand1 + '-' + hand2
        results = range_battle(battle_name)
        mean_equity = np.round(np.mean([x['EV'] for x in results.values()]), 3)
        print(battle_name, mean_equity)
        hand_results[battle_name] = mean_equity

    with open(file_path, 'w') as fp:
        json.dump(hand_results, fp)
