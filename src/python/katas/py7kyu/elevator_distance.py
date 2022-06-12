"""Kata url: https://www.codewars.com/kata/59f061773e532d0c87000d16."""

from typing import List


def elevator_distance(array: List[int]) -> int:
    return sum(abs(new - previous) for previous, new in zip(array, array[1:]))


def test_elevator_distance():
    assert elevator_distance([5, 2, 8]) == 9
    assert elevator_distance([1, 2, 3]) == 2
    assert elevator_distance([7, 1, 7, 1]) == 18
