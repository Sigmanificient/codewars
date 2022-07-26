"""Kata url: https://www.codewars.com/kata/57f609022f4d534f05000024."""

from typing import List


def stray(arr: List[int]) -> int:
    return min(arr, key=arr.count)


def test_stray():
    assert stray([1, 1, 1, 1, 1, 1, 2]) == 2
    assert stray([2, 3, 2, 2, 2]) == 3
    assert stray([3, 2, 2, 2, 2]) == 3
