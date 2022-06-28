"""Kata url: https://www.codewars.com/kata/55eca815d0d20962e1000106."""

from typing import List


def generate_range(_min: int, _max: int, step: int) -> List[int]:
    return list(range(_min, _max + 1, step))


def test_generate_range():
    assert generate_range(1, 10, 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert generate_range(-10, 1, 1) == [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1]
    assert generate_range(1, 15, 20) == [1]
    assert generate_range(1, 7, 2) == [1, 3, 5, 7]
    assert generate_range(0, 20, 3) == [0, 3, 6, 9, 12, 15, 18]
