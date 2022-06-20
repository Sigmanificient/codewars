"""Kata url: https://www.codewars.com/kata/5388f0e00b24c5635e000fc6."""

from typing import List


def swap_values(arr: List[int]) -> None:
    arr.reverse()


def test_swap_values():
    arr = [1, 2]
    swap_values(arr)
    assert arr == [2, 1]
