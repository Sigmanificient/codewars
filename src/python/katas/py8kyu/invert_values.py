"""Kata url: https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad."""

from typing import List


def invert(lst: List[int]) -> List[int]:
    return [-x for x in lst]


def test_invert():
    assert invert([]) == []
    assert invert([1, 2, 3, 4, 5]) == [-1, -2, -3, -4, -5]
    assert invert([1, -2, 3, -4, 5]) == [-1, 2, -3, 4, -5]
