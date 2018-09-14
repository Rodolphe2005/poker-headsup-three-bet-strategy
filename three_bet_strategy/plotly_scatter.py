import plotly as py
import plotly.graph_objs as go

from hand import Hand
from three_bet_strategy.call_equity import three_bet_equity, call_equity

hand = Hand(name='54o', combos=16)


def equities(steal, fold_percentage, hand):
    three_bet_value = three_bet_equity(
        hand,
        steal=steal,
        fold_percentage=fold_percentage)
    fold_value = -1
    call_value = call_equity(hand, steal)
    return fold_value, call_value, three_bet_value


f_range = range(20, 80, 2)
s_range = range(40, 100, 4)

z_values = [
    [
        round(equities(steal=s, fold_percentage=f, hand=hand)[2]+1,3)
        for f in f_range
    ]
    for s in s_range
]

z_text = [
    [
        str(round(equities(steal=s, fold_percentage=f, hand=hand)[2]+1,1))
        for f in f_range
    ]
    for s in s_range
]
hover_text = [
    [
        'Call equity: ' + str(round(
            call_equity(hand=hand, steal=s)
            , 3)) +
        '3bet equity: ' + str(round(
            three_bet_equity(hand=hand, steal=s, fold_percentage=f)
            , 3))
        for f in f_range
    ]
    for s in s_range
]


data = [
    go.Scatter(
        x=[f for f in f_range for s in s_range],
        y=[s for f in f_range for s in s_range],
        text=[str(f+s) for f in f_range for s in s_range],
        hoveron='points',
        hoverinfo='all',
        mode='markers+'
    )
]
layout = go.Layout(
    title='',
    xaxis=dict(
        title='Pourcentage de fold au 3bet',
    ),
    yaxis=dict(
        title='Pourcentage de raise au bouton',
    )
)
fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig)
