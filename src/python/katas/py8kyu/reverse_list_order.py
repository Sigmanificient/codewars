"""Kata url: https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b."""

from typing import List


def reverse_list(collection: List[int]) -> List[int]:
    return collection[::-1]


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_list([3, 1, 5, 4]) == [4, 5, 1, 3]
    assert reverse_list([3, 6, 9, 2]) == [2, 9, 6, 3]
    assert reverse_list([1]) == [1]
