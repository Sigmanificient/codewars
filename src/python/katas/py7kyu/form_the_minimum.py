"""Kata url: https://www.codewars.com/kata/5ac6932b2f317b96980000ca."""
from typing import List


def min_value(digits: List[int]) -> int:
    return int(''.join(map(str, sorted(set(digits)))))


def test_min_value():
    assert min_value([1, 3, 1]) == 13
    assert min_value([4, 7, 5, 7]) == 457
    assert min_value([4, 8, 1, 4]) == 148

    assert min_value([1] * 10 + [2]) == 12
    assert min_value([9] * 50) == 9

    assert min_value(list(range(10))) == 123456789
