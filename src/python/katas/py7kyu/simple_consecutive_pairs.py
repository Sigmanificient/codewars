"""Kata url: https://www.codewars.com/kata/5a3e1319b6486ac96f000049."""
from typing import List


def pairs(arr: List[int]) -> int:
    return sum(abs(x - y) == 1 for x, y in zip(arr[::2], arr[1::2]))


def test_pairs():
    assert pairs([1, 2, 5, 8, -4, -3, 7, 6, 5]) == 3
    assert pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94]) == 2
    assert pairs([81, 44, 80, 26, 12, 27, -34, 37, -35]) == 0
    assert pairs([-55, -56, -7, -6, 56, 55, 63, 62]) == 4
    assert pairs([73, 72, 8, 9, 73, 72]) == 3
