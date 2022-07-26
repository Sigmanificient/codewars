"""Kata url: https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c."""

from typing import List


def even_numbers(arr: List[int], n: int) -> List[int]:
    odds: List[int] = [x for x in arr if not x % 2]
    return odds[len(odds) - n :]


def test_even_and_odd():
    assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [4, 6, 8]
    assert even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) == [-8, 26]
    assert even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) == [6]
