import plotly as py
import plotly.figure_factory as ff

from hand import Hand
from three_bet_strategy.call_equity import three_bet_equity, call_equity

hand = Hand(name='82o', combos=16)


def color_number_for(steal, fold_percentage, hand):
    three_bet_value = three_bet_equity(
        hand,
        steal=steal,
        fold_percentage=fold_percentage)
    fold_value = -1
    call_value = call_equity(hand, steal)
    return color_number(fold_value, call_value, three_bet_value)


def color_number(fold_value, call_value, three_bet_value):
    return three_bet_value - fold_value


def send(value, to):
    a, b = to
    return a + max(0, min(1, value)) * (b - a)


def adjust_to_color_range(z_value):
    a = min(min(z_value))
    b = max(max(z_value))
    for i, _ in enumerate(z_value):
        for j, _ in enumerate(z_value[i]):
            z = z_value[i][j]
            if z < 0:
                r = 0.5 * (z - a) / (-a)
            else:
                r = 0.5 + 0.5 * z / b
            z_value[i][j] = r
            print(z, r)
    return z_value


f_range = range(20, 50, 1)
s_range = range(40, 100, 4)
z_value = [
    [
        color_number_for(steal=s, fold_percentage=f, hand=hand)
        for f in f_range
    ]
    for s in s_range
]
z_value = adjust_to_color_range(z_value)
z_text = [
    [
        str(round(color_number_for(steal=s, fold_percentage=f, hand=hand), 2))
        for f in f_range
    ]
    for s in s_range
]

def hover_text_of(hand, steal, fold_percentage):
    call_value = round(call_equity(hand=hand, steal=steal),3)
    three_bet_value = round(three_bet_equity(hand=hand, steal=steal, fold_percentage=fold_percentage),3)
    return f'Steal: {str(steal)}%<br>' \
           f'Fold to 3bet: {str(fold_percentage)}%<br>' \
           f'<br>' \
           f'Call equity: {str(call_value)}<br>' \
           f'3bet equity: {str(three_bet_value)}'

hover_text = [
    [
        hover_text_of(hand, steal=s, fold_percentage=f)
        for f in f_range
    ]
    for s in s_range
]

colorscale = [
    [0, "#cc2900"],
    [0.47, "#ffc2b3"],
    [0.53, "#d9f2e5"],
    [1, "#339964"],
]

fig = ff.create_annotated_heatmap(
    z=z_value,
    x=list(f_range),
    y=list(s_range),
    annotation_text=z_text,
    hoverinfo='text',
    text=hover_text,
    colorscale=colorscale,
    showscale=True
)
fig['layout'].update(
    title='',
    xaxis=dict(
        title='Pourcentage de fold au 3bet',
    ),
    yaxis=dict(
        title='Pourcentage de raise au bouton',
    )
)
py.offline.plot(fig)
