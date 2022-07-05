"""Kata url: https://www.codewars.com/kata/57aa218e72292d98d500240f."""

from math import sqrt


def heron(a: int, b: int, c: int) -> float:
    s: float = (a + b + c) / 2
    return round(sqrt(s * (s - a) * (s - b) * (s - c)), 2)


def test_heron():
    assert heron(3, 4, 5) == 6
    assert heron(5, 12, 13) == 30
