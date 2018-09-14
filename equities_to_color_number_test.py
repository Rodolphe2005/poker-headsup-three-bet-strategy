from equities_to_color_number import equities_to_color_number


def test_there_are_no_folds_possible():
    equities = [
        [(-1, 2, 0), (-1, 0, 0)],
        [(-1, 0, 3), (-1, 0, 3)]
    ]
    colorscale, z_values = equities_to_color_number(equities)
