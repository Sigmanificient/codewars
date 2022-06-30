"""Kata url: https://www.codewars.com/kata/55edaba99da3a9c84000003b."""

from typing import List


def divisible_by(numbers: List[int], divisor: int) -> List[int]:
    return [n for n in numbers if (n / divisor).is_integer()]


def test_divisible_by():
    assert divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
    assert divisible_by([1, 2, 3, 4, 5, 6], 3) == [3, 6]
    assert divisible_by([0, 1, 2, 3, 4, 5, 6], 4) == [0, 4]
    assert divisible_by([0], 4) == [0]
    assert divisible_by([1, 3, 5], 2) == []
    assert divisible_by([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
