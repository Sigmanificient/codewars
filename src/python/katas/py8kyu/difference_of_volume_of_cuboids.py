"""Kata url: https://www.codewars.com/kata/58cb43f4256836ed95000f97."""

from typing import List


def mul(x: List[int]) -> int:
    """Multiply every element of an array together."""
    r = 1
    for k in x:
        r *= k
    return r


def find_difference(a: List[int], b: List[int]) -> int:
    return abs(mul(a) - mul(b))


def test_find_difference():
    assert find_difference([1, 2, 3], [1, 2, 3]) == 0
    assert find_difference([3, 2, 5], [1, 4, 4]) == 14
    assert find_difference([9, 7, 2], [5, 2, 2]) == 106
