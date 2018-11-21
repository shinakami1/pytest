import pytest
from cashback_homework_1 import calculate_cashback

@pytest.mark.parametrize('input, expected', [
        ([10_000, 0 ,2_000], 700.0),
        ([0, 0, 1_000], 300.0),
        ([310_000, 0, 60_000], 9000.0),
        ([0, 10_000, 0], 500.0),
])
def test_calculate_cashback(input, expected):
    actual = calculate_cashback(*input)
    assert expected == actual