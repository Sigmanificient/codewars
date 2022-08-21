"""Kata url: https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4."""
from typing import List


def least_larger(a: List[int], i: int) -> int:
    mn = a[i]

    least = min((k for k in a if k > mn), default=None)
    if least is None:
        return -1

    return a.index(least)


def test_least_larger():
    assert least_larger([4, 1, 3, 5, 6], 0) == 3
    assert least_larger([4, 1, 3, 5, 6], 4) == -1
    assert least_larger([1, 3, 5, 2, 4], 0) == 3
