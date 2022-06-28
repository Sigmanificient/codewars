"""Kata url: https://www.codewars.com/kata/5f70c883e10f9e0001c89673."""

from typing import List


def flip(d: str, a: List[int]) -> List[int]:
    return sorted(a)[::-1 if d == 'L' else 1]


def test_flip():
    assert flip('R', [3, 2, 1, 2]) == [1, 2, 2, 3]
    assert flip('L', [1, 4, 5, 3, 5]) == [5, 5, 4, 3, 1]
