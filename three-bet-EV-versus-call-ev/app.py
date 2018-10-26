from flask import Flask, json, jsonify, request
from flask_cors import CORS
from three_bet_strategy.call_equity import three_bet_equity, call_equity
from hand import Hand
from hand_battle import possible_hands, possible_cards, combos_of

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def hello():
    steal = int(request.json['steal'])
    fold3bet = int(request.json['fold3bet'])
    fourbet = int(request.json['fourbet'])
    oop_penalty = int(request.json['oop_penalty'])
    steal_size = float(request.json['steal_size'])
    threebet_size = float(request.json['threebet_size'])
    response = jsonify([
        equities_of('T9o', steal, fold3bet, fourbet, oop_penalty, steal_size, threebet_size),
        equities_of('JTo', steal, fold3bet, fourbet, oop_penalty, steal_size, threebet_size),
        equities_of('98o', steal, fold3bet, fourbet, oop_penalty, steal_size, threebet_size),
        equities_of('87o', steal, fold3bet, fourbet, oop_penalty, steal_size, threebet_size),

    ])
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response.json)
    return response


def equities_of(hand_name, steal, fold3bet, fourbet, oop_penalty, steal_size, threebet_size):
    fold_equity = -1
    hand = Hand(name=hand_name,
                combos=combos_of[hand_name[2:]])
    return {
        "x": call_equity(hand, steal, oop_penalty, steal_size) - fold_equity,
        "y": three_bet_equity(
            hand=hand,
            steal=steal,
            fold_percentage=fold3bet,
            fourbet=fourbet,
            oop_penalty=oop_penalty,
            steal_size=steal_size,
            threebet_size=threebet_size
        ) - fold_equity,
        "hand": hand_name}


app.run(debug=True)
