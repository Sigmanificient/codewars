"""Kata url: https://www.codewars.com/kata/57cc981a58da9e302a000214."""
from typing import List


def small_enough(array: List[int], limit: int) -> bool:
    return not next(filter(limit.__lt__, array), 0)


def test_small_enough():
    assert small_enough([66, 101], 200)
    assert not small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100)
    assert small_enough([101, 45, 75, 105, 99, 107], 107)
    assert small_enough([80, 117, 115, 104, 45, 85, 112, 115], 120)
    assert not small_enough([1, 1, 1, 1, 1, 2], 1)
    assert not small_enough([78, 33, 22, 44, 88, 9, 6], 87)
    assert small_enough([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
    assert small_enough([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 12)
