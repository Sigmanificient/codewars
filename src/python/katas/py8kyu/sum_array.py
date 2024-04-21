"""Kata url: https://www.codewars.com/kata/53dc54212259ed3d4f00071c."""

from typing import Sequence


def sum_array(a: Sequence[int | float]) -> int | float:
    return sum(a)


def test_sum_array():
    assert sum_array([]) == 0
    assert sum_array([1, 2, 3]) == 6
    assert abs(sum_array([1.1, 2.2, 3.3]) - 6.6) < 0.001
    assert sum_array([4, 5, 6]) == 15
    assert sum_array(range(101)) == 5050