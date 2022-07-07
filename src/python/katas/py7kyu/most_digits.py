"""Kata url: https://www.codewars.com/kata/58daa7617332e59593000006."""

from typing import List


def find_longest(arr: List[int]) -> int:
    return max(arr, key=lambda x: len(str(x)))


def test_find_longest():
    assert find_longest([1, 10, 100]) == 100
    assert find_longest([9000, 8, 800]) == 9000
    assert find_longest([8, 900, 500]) == 900
    assert find_longest([3, 40000, 100]) == 40000
    assert find_longest([1, 200, 100000]) == 100000
    assert find_longest([1, 200, 999, 500, 2, 3]) == 200
