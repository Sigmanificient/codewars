"""Kata url: https://www.codewars.com/kata/59f061773e532d0c87000d16."""

from typing import List


def elevator_distance(array: List[int]) -> int:
    return sum(abs(new - previous) for previous, new in zip(array, array[1:]))
