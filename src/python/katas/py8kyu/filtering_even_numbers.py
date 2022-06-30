"""Kata url: https://www.codewars.com/kata/566dc566f6ea9a14b500007b."""

from typing import List


def kata_13_december(lst: List[int]) -> List[int]:
    return [x for x in lst if x % 2]


def test_kata_13_december():
    assert kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]) == [1, 3, 5, 7]
    assert kata_13_december([1, 2, 2, 2, 4, 3, 4]) == [1, 3]
