"""Kata url: https://www.codewars.com/kata/585d7d5adb20cf33cb000235."""

from typing import List, TypeVar

T = TypeVar('T')


def find_uniq(arr: List[T]) -> T:
    return min(set(arr), key=arr[:3].count)


def test_find_uniq():
    assert find_uniq([1, 1, 1, 2, 1, 1]) == 2
    assert (find_uniq([0, 0, 0.55, 0, 0]) - 0.55) < 0.0001
    assert find_uniq([3, 10, 3, 3, 3]) == 10
    assert find_uniq([1] * 999999 + [2]) == 2