"""Kata url: https://www.codewars.com/kata/52f3149496de55aded000410."""


def sum_digits(number: int) -> int:
    return sum(map(int, str(abs(number))))


def test_sum_digits():
    assert sum_digits(10) == 1
    assert sum_digits(99) == 18
    assert sum_digits(-32) == 5
