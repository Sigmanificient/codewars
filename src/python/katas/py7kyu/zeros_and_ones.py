"""Kata url: https://www.codewars.com/kata/578553c3a1b8d5c4030003."""

from typing import List


def binary_array_to_number(arr: List[int]) -> int:
    return int("".join(map(str, arr)), 2)


def test_binary_array_to_number():
    assert binary_array_to_number([0, 0, 0, 1]) == 1
    assert binary_array_to_number([1, 1, 0, 1]) == 13
    assert binary_array_to_number([1, 0, 0, 1, 0, 0, 1, 1, 1, 0]) == 590
    assert binary_array_to_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
