"""Kata url: https://www.codewars.com/kata/595aa94353e43a8746000120."""
from typing import List


def find_deleted_number(arr: List[int], mixed_arr: List[int]) -> int:
    if len(arr) == len(mixed_arr):
        return 0

    if not mixed_arr:
        return arr[0]

    s = sorted(mixed_arr)
    return next((i for i, j in zip(arr, s) if i != j), arr[-1])


def test_find_deleted_number():
    assert find_deleted_number([], []) == 0
    assert find_deleted_number([1], []) == 1
    assert find_deleted_number(
        [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 7, 9, 4, 8, 1, 2, 3]
    ) == 6
    assert find_deleted_number(
        [1, 2, 3, 4, 5, 6, 7], [2, 3, 6, 1, 5, 4, 7]
    ) == 0
    assert find_deleted_number(
        [1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 7, 6, 9, 4, 8, 1, 2, 3]
    ) == 0
