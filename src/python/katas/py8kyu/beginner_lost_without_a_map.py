"""Kata url: https://www.codewars.com/kata/57f781872e3d8ca2a000007e."""

from typing import List


def maps(a: List[int]) -> List[int]:
    return [x * 2 for x in a]


def test_maps():
    assert maps([]) == []
    assert maps([1, 2, 3]) == [2, 4, 6]
    assert maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
