from collections import defaultdict

import requests
import json
import time

all_hands = []
d = defaultdict(dict)

card1, card2 = 'Js', 'Jc'
card3, card4 = 'Kd', 'Kh'


def query(card1, card2, card3, card4):
    time.sleep(1)
    r = requests.get('https://www.pokerlistings.com/api/v1/poker/holdem/odds?'
                     f'&player_1={card1},{card2}&player_2={card3},{card4}')
    x = json.loads(r.content)['results']['players']
    assert x[0]['player'] == 1
    return x[0]['results']

result = query(card1, card2, card3, card4)

for p in all permutations:
    suits = card1[1], card2[1], card3[1], card4[1]
    s1, s2, s3, s4 = permute(suits)
    hand1 = card1[0] + s1 + card2[0] + s2
    hand2 = card3[0] + s3 + card4[0] + s4
    d[hand1][hand2] = result

with open(f'data/{card1+card2}.json', 'w') as fp:
    json.dump(d, fp)
