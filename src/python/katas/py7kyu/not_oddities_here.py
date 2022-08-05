"""Kata url: https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce."""

from typing import List


def no_odds(values: List[int]) -> List[int]:
    return [x for x in values if not x % 2]


def test_no_odds():
    assert no_odds([0, 1]) == [0]
    assert no_odds([0, 1, 2, 3]) == [0, 2]
    assert no_odds([1, 3, 5, 7, 9]) == []
    assert no_odds([0, 2, 4, 6, 8, 10]) == [0, 2, 4, 6, 8, 10]
    assert no_odds([2, 4, 8, 6, 0]) == [2, 4, 8, 6, 0]
    assert no_odds([]) == []
