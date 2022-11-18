"""Kata url: https://www.codewars.com/kata/564f458b4d75e24fc9000041."""


def remainder(dividend, divisor):
    while dividend >= divisor:
        dividend -= divisor
    return dividend


def test_remainder():
    assert remainder(3, 2) == 1
    assert remainder(19, 2) == 1
    assert remainder(10, 2) == 0
    assert remainder(34, 7) == 6
    assert remainder(27, 5) == 2
