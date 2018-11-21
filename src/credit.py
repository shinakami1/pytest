def calculate_credit(initial_amount, monthly_rate, credit_term):
    """
    >>> calculate_credit(200_000, 0.2 , 12)
    18527

    >>> calculate_credit(200_000, 0.2 , 24)
    10179

    >>> calculate_credit(1_100_000, 0.23 , 13)
    96399
    """

    monthly_rate = monthly_rate/12

    monthly_payment = initial_amount * (monthly_rate + monthly_rate / (((1 + monthly_rate) ** credit_term) - 1))


    # x - monthly_payment (сумма ежемесячного платежа)
    # p - monthly_rate (ежемесячная ставка)
    # s - initial_amount (первоначальная сумма)
    # n - credit term (срок кредита в мес)

    return round(monthly_payment)

calculate_credit(200_000, 0.2, 24)

print(calculate_credit(200_000, 0.2, 24))
