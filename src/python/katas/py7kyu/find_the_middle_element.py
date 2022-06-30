"""Kata url: https://www.codewars.com/kata/545a4c5a61aa4c6916000755."""
from typing import List


def gimme(arr: List[int]) -> int:
    return arr.index(sorted(arr)[1])


def test_gimme():
    assert gimme([2, 3, 1]) == 0, 'Finds the index of middle element'
    assert gimme([5, 10, 14]) == 1, 'Finds the index of middle element'
