from collections import defaultdict

import requests
import json
import time

all_hands = []
d = defaultdict(dict)

card1, card2 = 'Js', 'Jc'
card3, card4 = 'Kd', 'Kh'


def query(card1, card2, card3, card4):
    time.sleep(0)
    r = requests.get('https://www.pokerlistings.com/api/v1/poker/holdem/odds?'
                     f'&player_1={card1},{card2}&player_2={card3},{card4}')
    x = json.loads(r.content)['results']['players']
    assert x[0]['player'] == 1
    return x[0]['results']
