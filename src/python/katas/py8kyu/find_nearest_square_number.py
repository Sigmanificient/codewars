"""Kata url: https://www.codewars.com/kata/5a805d8cafa10f8b930005ba."""

from math import sqrt


def nearest_sq(n: int) -> int:
    return round(sqrt(n)) ** 2


def test_nearest_sq():
    assert nearest_sq(1) == 1
    assert nearest_sq(2) == 1
    assert nearest_sq(10) == 9
    assert nearest_sq(111) == 121
    assert nearest_sq(9999) == 10000
