"""Kata url: https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9."""
from typing import List


def up_array(arr: List[int]) -> List[int]:
    if not arr:
        return

    for item in arr:
        if item < 0 or item > 9:
            return

    x = ''.join(map(str, arr))
    return [int(k) for k in str(int(x) + 1)]


def test_up_array():
    assert up_array([5, 7, 4]) == [5, 7, 5]
    assert up_array([0]) == [1]
    assert up_array([1, 0, 0, 0]) == [1, 0, 0, 1]
    assert up_array([9, 9, 9]) == [1, 0, 0, 0]
    assert up_array([2, 1, 4, 7, 4, 8, 3, 6, 4, 7]) == [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]

    assert up_array([1, 2, 33]) is None
    assert up_array([1, 2, -1]) is None
    assert up_array([10]) is None
    assert up_array([]) is None
