"""Kata url: https://www.codewars.com/kata/576b93db1129fcf2200001e6."""

from typing import Optional, List


def sum_array(arr: Optional[List[int]]) -> int:
    return sum(sorted(arr)[1:-1]) if arr else 0


def test_sum_array():
    assert sum_array(None) == 0
    assert sum_array([]) == 0

    assert sum_array([3]) == 0
    assert sum_array([-3]) == 0

    assert sum_array([3, 5]) == 0
    assert sum_array([-3, -5]) == 0

    assert sum_array([6, 2, 1, 8, 10]) == 16
    assert sum_array([6, 0, 1, 10, 10]) == 17
    assert sum_array([-6, -20, -1, -10, -12]) == -28
    assert sum_array([-6, 20, -1, 10, -12]) == 3
