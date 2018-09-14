min_color_three_bet = "#555555"
max_color_three_bet = "#55FF55"

max_call_value = 3
max_three_bet_value = 3


def equities_to_color_number(equities):


    return colorscale, z_values



def color_number(fold_value, call_value, three_bet_value):
    if max(call_value, three_bet_value) < fold_value - 0.2:
        return 0
    elif max(call_value, three_bet_value) < fold_value:
        return 0.1
    else:
        if call_value >= three_bet_value:
            return send((call_value - fold_value) / (max_call_value - fold_value), to=(0.2, 0.5))
        else:
            return send((three_bet_value - fold_value) / (max_three_bet_value - fold_value), to=(0.6, 0.9))


def send(value, to):
    a, b = to
    return a + max(0, min(1, value)) * (b - a)
