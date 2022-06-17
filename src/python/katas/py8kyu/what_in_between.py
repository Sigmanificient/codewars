"""Kata url: https://www.codewars.com/kata/55ecd718f46fba02e5000029."""

from typing import List


def between(a: int, b: int) -> List[int]:
    return list(range(a, b + 1))


def test_between():
    assert between(1, 3) == [1, 2, 3]
    assert between(1, 5) == [1, 2, 3, 4, 5]
    assert between(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
