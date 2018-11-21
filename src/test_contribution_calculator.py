from contribution_calculator import calculate_contribution

def test_calculate_contribution():
    test_case = [
        (756000.0, 700_000, 1, 0.08),
        ('Error', 100_000, 0.5, 0.08),
        ('Error', 100_000, 2.1, 0.08),
    ]

    for x in test_case:
        assert x[0] == calculate_contribution(x[1], x[2], x[3])