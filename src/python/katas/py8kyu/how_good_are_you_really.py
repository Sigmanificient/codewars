"""Kata url: https://www.codewars.com/kata/5601409514fc93442500010b."""

from typing import List


def better_than_average(class_points: List[int], your_points: int) -> bool:
    return sum(class_points) / len(class_points) < your_points


def test_better_than_average():
    assert better_than_average([2, 3], 5)
    assert better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)
    assert better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69)
    assert not better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50)
