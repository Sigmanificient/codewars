"""Kata url: https://www.codewars.com/kata/60cf559c068ae600468f8e5a."""


def reverse_float_decimal(n: float) -> float:
    return int(n) + float(f'0.{str(round(n % 1, 5))[2:][::-1]}')


def test_reverse_float_decimal():
    assert reverse_float_decimal(2.5) == 2.5
    assert reverse_float_decimal(1.12345) == 1.54321
    assert reverse_float_decimal(7.0007) == 7.7
