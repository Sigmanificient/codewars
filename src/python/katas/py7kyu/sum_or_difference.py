"""Kata url: https://www.codewars.com/kata/60ff7bf19347db00319e7afc."""


def sum_diff(a: int, b: int, c: int) -> int:
    return (b + c) if a % 2 else max(b, c) - min(b, c)


def test_sum_diff():
    assert sum_diff(3, 2, 5) == 7
    assert sum_diff(3, 2, 3) == 5
