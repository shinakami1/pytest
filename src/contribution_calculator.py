def calculate_contribution (deposit_amount, term_years ,interest_rate):
    """
    >>> calculate_contribution (700_000, 1, 0.08)
    756000.0

    >>> calculate_contribution(100_000, 0.5, 0.08)
    'Error'

    >>> calculate_contribution(100_000, 2.1, 0.08)
    'Error'
    """
    if term_years % 1 != 0:
        return  "Error"

    total_amoun = (deposit_amount * term_years * interest_rate)+ deposit_amount

    return total_amoun

calculate_contribution (700_000, 1, 0.08)

print(calculate_contribution (700_000, 1, 0.08))
