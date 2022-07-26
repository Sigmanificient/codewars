"""Kata url: https://www.codewars.com/kata/55a2d7ebe362935a210000b2."""

from typing import List


def find_smallest_int(arr: List[int]) -> int:
    return min(arr)


def test_find_smallest_int():
    assert find_smallest_int([78, 56, 232, 12, 11, 43]) == 11
    assert find_smallest_int([78, 56, -2, 12, 8, -33]) == -33
    assert find_smallest_int([0, 1 - 2**64, 2**64]) == 1 - 2**64
    assert find_smallest_int([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
