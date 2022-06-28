"""Kata url: https://www.codewars.com/kata/56a1c074f87bc2201200002e."""
from typing import List


def smaller(arr: List[int]) -> List[int]:
    return [
        sum(True for x in arr[c:] if x < i)
        for c, i in enumerate(arr)
    ]


def test_smaller():
    assert smaller([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
    assert smaller([1, 2, 3]) == [0, 0, 0]
    assert smaller([1, 2, 0]) == [1, 1, 0]
    assert smaller([1, 2, 1]) == [0, 1, 0]
    assert smaller([1, 1, -1, 0, 0]) == [3, 3, 0, 0, 0]
    assert smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]) == [4, 1, 5, 5, 0, 0, 0, 0, 0]
