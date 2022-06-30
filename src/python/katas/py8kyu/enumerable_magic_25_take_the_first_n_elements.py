"""Kata url: https://www.codewars.com/kata/545afd0761aa4c3055001386."""

from typing import List


def take(arr: List[int], n: int) -> List[int]:
    return arr[:n]


def test_take():
    assert take([0, 1, 2, 3, 5, 8, 13], 3) == [0, 1, 2]
    assert take([0, 1, 2, 3, 5, 8, 13], 2) == [0, 1]
    assert take([0, 1, 2, 3, 5, 8, 13], 1) == [0]
    assert take([0, 1, 2, 3, 5, 8, 13], 0) == []

    assert take([1, 3, 5, 7, 9], 2) == [1, 3]
    assert take([1, 3, 5, 7, 9], 3) == [1, 3, 5]
    assert take([1, 3, 5, 7, 9], 4) == [1, 3, 5, 7]
