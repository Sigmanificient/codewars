"""Kata url: https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9."""

from typing import List


def row_weights(array: List[int]) -> List[int]:
    return sum(array[::2]), sum(array[1::2])


def test_row_weights():
    assert row_weights([80]) == (80, 0)
    assert row_weights([100, 50]) == (100, 50)
    assert row_weights([50, 60, 70, 80]) == (120, 140)
    assert row_weights([13, 27, 49]) == (62, 27)
    assert row_weights([70, 58, 75, 34, 91]) == (236, 92)
    assert row_weights([29, 83, 67, 53, 19, 28, 96]) == (211, 164)
    assert row_weights([0]) == (0, 0)
    assert row_weights([100, 51, 50, 100]) == (150, 151)
    assert row_weights([39, 84, 74, 18, 59, 72, 35, 61]) == (207, 235)
    assert row_weights([0, 1, 0]) == (0, 1)
