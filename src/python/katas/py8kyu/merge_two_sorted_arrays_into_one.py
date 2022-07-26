"""Kata url: https://www.codewars.com/kata/5899642f6e1b25935d000161."""


from typing import List


def merge_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    return sorted(set(arr1 + arr2))


def test_merge_arrays():
    assert merge_arrays([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_arrays([1, 3, 5, 7, 9], [10, 8, 6, 4, 2]) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ]
    assert merge_arrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12]) == [
        1,
        2,
        3,
        4,
        5,
        7,
        9,
        10,
        11,
        12,
    ]
