"""Kata url: https://www.codewars.com/kata/563e320cee5dddcf77000158."""

from typing import List


def get_average(marks: List[int]) -> int:
    return sum(marks) // len(marks)


def test_get_average():
    assert get_average([2, 2, 2, 2]) == 2
    assert get_average([1, 5, 87, 45, 8, 8]) == 25
    assert get_average([2, 5, 13, 20, 16, 16, 10]) == 11
    assert (
        get_average([1, 2, 15, 15, 17, 11, 12, 17, 17, 14, 13, 15, 6, 11, 8, 7]) == 11
    )
