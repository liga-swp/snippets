"""Example tests."""


def add(num1, num2):
    """Compute the sum of two values."""
    return num1 + num2


def test_add_2_plus_2():
    num1, num2 = 2.0, 2.0

    my_result = add(num1, num2)
    result = num1 + num2

    assert my_result == result


def test_add_100_plus_neg1():
    num1, num2 = 100.0, -1.0

    my_result = add(num1, num2)
    result = num1 + num2

    assert my_result == result
