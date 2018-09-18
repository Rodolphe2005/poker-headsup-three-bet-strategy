import os
from flask import render_template, Flask

from hand import Hand
from hand_battle import possible_hands, possible_cards, combos_of
from range_battle import range_battle
from three_bet_strategy.call_equity import three_bet_equity, call_equity
from utils import do_profile

current_folder = os.path.dirname(__file__)


def generate_hand_properties(steal, fold_percentage):
    for card1, card2, possible_suit in possible_hands():
        index1 = possible_cards.index(card1)
        index2 = possible_cards.index(card2)
        if possible_suit == 's':
            index1, index2 = index2, index1
        hand = Hand(name=card1 + card2 + possible_suit, combos=combos_of[possible_suit])
        yield {
            "name": hand.name,
            "i": 13 - index1,
            "j": 13 - index2,
            "call_value": call_equity(hand, steal=steal),
            "three_bet_value": three_bet_equity(hand=hand, steal=steal, fold_percentage=fold_percentage),
            "steal": steal,
            "fold_percentage": fold_percentage,
        }


@do_profile(follow=[range_battle])
def create_three_bet_strategy_dataviz():
    app = Flask('myapp', template_folder=current_folder)
    with app.app_context():
        min_steal = 30
        max_steal = 70
        min_fold = 25
        max_fold = 45

        html_page = render_template(
            'three_bet_strategy.html',
            data_points=[
                hand_as_json
                for steal in range(min_steal, max_steal + 1, 1)
                for fold_percentage in range(min_fold, max_fold, 1)
                for hand_as_json in generate_hand_properties(steal=steal, fold_percentage=fold_percentage)
            ],
            min_steal=min_steal,
            max_steal=max_steal,
            min_fold=min_fold,
            max_fold=max_fold
        )

        with open(current_folder + '/generated_three_bet_strategy.html', 'w') as fp:
            fp.write(html_page)

create_three_bet_strategy_dataviz()