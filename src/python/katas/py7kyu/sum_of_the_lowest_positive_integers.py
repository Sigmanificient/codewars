"""Kata url: https://www.codewars.com/kata/558fc85d8fd1938afb000014."""
from typing import List


def sum_two_smallest_numbers(numbers: List[int]) -> int:
    a, b, *_ = sorted(numbers)
    return a + b


def test_sum_tow_smallest():
    assert sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13
    assert sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19
    assert sum_two_smallest_numbers([25, 42, 12, 18, 22]) == 30
