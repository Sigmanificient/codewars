"""Kata url: https://www.codewars.com/kata/5a2be17aee1aaefe2a000151."""


from typing import List


def array_plus_array(arr1: List[int], arr2: List[int]) -> int:
    return sum(arr1 + arr2)


def test_array_plus_array():
    assert array_plus_array([1, 2, 3], [4, 5, 6]) == 21
    assert array_plus_array([-1, -2, -3], [-4, -5, -6]) == -21
    assert array_plus_array([0, 0, 0], [4, 5, 6]) == 15
    assert array_plus_array([100, 200, 300], [400, 500, 600]) == 2100
