"""Kata url: https://www.codewars.com/kata/59fa8e2646d8433ee200003f."""
from typing import NoReturn, List


def sort_by_bit(arr: List[int]) -> NoReturn:
    arr.sort(key=lambda k: (f"{k:b}".count('1'), k))


def test_sort_by_bit():
    a = [3, 8, 3, 6, 5, 7, 9, 1]
    sort_by_bit(a)
    assert a == [1, 8, 3, 3, 5, 6, 9, 7]

    b = [9, 4, 5, 3, 5, 7, 2, 56, 8, 2, 6, 8, 0]
    sort_by_bit(b)
    assert b == [0, 2, 2, 4, 8, 8, 3, 5, 5, 6, 9, 7, 56]
