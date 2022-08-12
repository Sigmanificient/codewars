"""Kata url: https://www.codewars.com/kata/59590976838112bfea0000fa."""
from typing import List


def beggars(values: List[int], n: int) -> List[int]:
    totals = [0] * n
    if not totals:
        return totals

    for c, v in enumerate(values):
        totals[c % n] += v

    return totals


def test_beggars():
    assert beggars([1, 2, 3, 4, 5], 1) == [15]
    assert beggars([1, 2, 3, 4, 5], 2) == [9, 6]
    assert beggars([1, 2, 3, 4, 5], 3) == [5, 7, 3]
    assert beggars([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5, 0]
    assert beggars([1, 2, 3, 4, 5], 0) == []
