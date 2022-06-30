"""Kata url: https://www.codewars.com/kata/577a98a6ae28071780000989."""

from typing import List


def minimum(arr: List[int]) -> int:
    return min(arr)


def maximum(arr: List[int]) -> int:
    return max(arr)


def test_minimum():
    assert minimum([-52, 56, 30, 29, -54, 0, -110]) == -110
    assert minimum([42, 54, 65, 87, 0]) == 0
    assert minimum([1, 2, 3, 4, 5, 10]) == 1
    assert minimum([-1, -2, -3, -4, -5, -10]) == -10
    assert minimum([9]) == 9


def test_maximum():
    assert maximum([-52, 56, 30, 29, -54, 0, -110]) == 56
    assert maximum([4, 6, 2, 1, 9, 63, -134, 566]) == 566
    assert maximum([5]) == 5
    assert maximum([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]) == 555
    assert maximum([9]) == 9
