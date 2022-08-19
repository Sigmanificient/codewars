"""Kata url: https://www.codewars.com/kata/559cc2d2b802a5c94700000c."""
from typing import List


def consecutive(arr: List[int]) -> int:
    return max(arr) - min(arr) + 1 - len(arr) if arr else 0


def test_consecutive():
    assert consecutive([4, 8, 6]) == 2
    assert consecutive([1, 2, 3, 4]) == 0
    assert consecutive([]) == 0
    assert consecutive([1]) == 0
    assert consecutive([-10]) == 0
    assert consecutive([1, -1]) == 1
    assert consecutive([-10, -9]) == 0
    assert consecutive([0]) == 0
    assert consecutive([10, -10]) == 19
    assert consecutive([-10, 10]) == 19
