def calculate_cashback(usual, elevated, special):
    """
    >>> calculate_cashback(10_000, 0 ,2_000)
    700.0

    >>> calculate_cashback(0, 0, 1_000)
    300.0

    >>> calculate_cashback(310_000, 0, 60_000)
    9000.0

    >>> calculate_cashback(0, 10_000, 0)
    500.0

    """
    pr_usual = 0.01
    pr_elevated = 0.05
    pr_special = 0.3

    cashback = 0

    if usual * pr_usual < 3_000:
        cashback = cashback + usual * pr_usual
    else:
        cashback = cashback + 3_000

    cashback = cashback + elevated * pr_elevated

    if special * pr_special < 6_000:
        cashback = cashback + special * pr_special
    else:
        cashback = cashback + 6_000

    #cashback = usual * pr_usual + elevated * pr_elevated + special * pr_special

    return cashback

print(calculate_cashback(310_000, 0, 60_000))

