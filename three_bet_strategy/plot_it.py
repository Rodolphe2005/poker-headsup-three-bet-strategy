import plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

from hand import Hand
from three_bet_strategy.call_equity import fold_equity, three_bet_equity


def diff_three_bet_with_fold(steal, fold_percentage):
    three_bet_value = three_bet_equity(
        Hand(name='54o', combos=16),
        steal=steal,
        fold_percentage=fold_percentage)
    if three_bet_value is None:
        return None
    return three_bet_value - fold_equity()


f_range = range(5, 100, 5)
s_range = range(5, 100, 5)

trace = go.Heatmap(
    z=[
        [
            diff_three_bet_with_fold(steal=s, fold_percentage=f)
            for f in range(5, 100, 5)
        ]
        for s in range(5, 100, 5)
    ],
    x=list(f_range),
    y=list(s_range),
    name='test',
    text=[
        [
            'Fold pourcentage : ' + str(f) + '<br>' +
            'Raise au bouton : ' + str(s)
            for f in range(5, 100, 5)
        ]
        for s in range(5, 100, 5)
    ],
    colorscale='Viridis'
)
layout = go.Layout(
    title='Strategie de 3 bet avec 54o',
    xaxis=dict(
        title='Pourcentage de fold au 3bet',
    ),
    yaxis=dict(
        title='Pourcentage de raise au bouton',
    )
)
data = [trace]
fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig)

print(diff_three_bet_with_fold(steal=75, fold_percentage=15))
