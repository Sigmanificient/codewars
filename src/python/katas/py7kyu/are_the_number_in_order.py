"""Kata url: https://www.codewars.com/kata/56b7f2f3f18876033f000307."""
from typing import List


def in_asc_order(arr: List[int]) -> bool:
    return arr == sorted(arr)


assert in_asc_order([1, 2])
assert not in_asc_order([2, 1])
assert in_asc_order([1, 2, 3])
assert not in_asc_order([1, 3, 2])
assert in_asc_order([1, 4, 13, 97, 508, 1047, 20058])
assert not in_asc_order([56, 98, 123, 67, 742, 1024, 32, 90969])
