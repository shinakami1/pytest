import pytest
from credit import calculate_credit

@pytest.mark.parametrize('input, expected', [
        ([200_000, 0.2 , 12], 18527),
        ([200_000, 0.2 , 24], 10179),
        ([1_100_000, 0.23, 13], 96399),
])
def test_calculate_credit(input, expected):
    actual = calculate_credit(*input)
    assert expected == actual
