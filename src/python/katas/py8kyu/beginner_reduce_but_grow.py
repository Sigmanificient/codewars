"""Kata url: https://www.codewars.com/kata/57f780909f7e8e3183000078."""

from typing import List


def grow(arr: List[int]) -> int:
    a: int = 1
    for b in arr:
        a *= b
    return a


def test_grow():
    assert grow([1, 2, 3]) == 6
    assert grow([4, 1, 1, 1, 4]) == 16
    assert grow([2, 2, 2, 2, 2, 2]) == 64