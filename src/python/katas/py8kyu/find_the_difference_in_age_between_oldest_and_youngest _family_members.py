"""Kata url: https://www.codewars.com/kata/5720a1cb65a504fdff0003e2."""

from typing import Tuple


def difference_in_ages(ages) -> Tuple[int, int, int]:
    mx = max(ages)
    mn = min(ages)
    return mn, mx, mx - mn


def test_difference_in_ages():
    assert difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]) == (3, 88, 85)
    assert difference_in_ages([5, 8, 72, 98, 41, 16, 55]) == (5, 98, 93)
    assert difference_in_ages([57, 99, 14, 32]) == (14, 99, 85)
    assert difference_in_ages([62, 0, 3, 77, 88, 102, 26, 44, 55]) == (0, 102, 102)
    assert difference_in_ages([2, 44, 34, 67, 88, 76, 31, 67]) == (2, 88, 86)
    assert difference_in_ages([46, 86, 33, 29, 87, 47, 28, 12, 1, 4, 78, 92]) == (1, 92, 91)
    assert difference_in_ages([66, 73, 88, 24, 36, 65, 5]) == (5, 88, 83)
