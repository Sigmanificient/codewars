"""Kata url: https://www.codewars.com/kata/580a4734d6df748060000045."""

from typing import List


def is_sorted_and_how(arr: List[int]) -> str:
    s = sorted(arr)
    if s == arr:
        return 'yes, ascending'
    elif s == arr[::-1]:
        return 'yes, descending'

    return 'no'


def test_is_sorted_and_how():
    assert is_sorted_and_how([1, 2]) == 'yes, ascending'
    assert is_sorted_and_how([15, 7, 3, -8]) == 'yes, descending'
    assert is_sorted_and_how([4, 2, 30]) == 'no'
