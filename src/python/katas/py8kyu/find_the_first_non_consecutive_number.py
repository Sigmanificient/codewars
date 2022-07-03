"""Kata url: https://www.codewars.com/kata/58f8a3a27a5c28d92e000144."""

from typing import List, Optional


def first_non_consecutive(arr: List[int]) -> Optional[int]:
    return next((fol for i, fol in zip(arr, arr[1:])if i + 1 != fol), None)


def test_first_non_consecutive():
    assert first_non_consecutive([1, 2, 3, 4, 6, 7, 8]) == 6
    assert first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]) is None
    assert first_non_consecutive([4, 6, 7, 8, 9, 11]) == 6
    assert first_non_consecutive([4, 5, 6, 7, 8, 9, 11]) == 11
    assert first_non_consecutive([31, 32]) is None
    assert first_non_consecutive([-3, -2, 0, 1]) == 0
    assert first_non_consecutive([-5, -4, -3, -1]) == -1
