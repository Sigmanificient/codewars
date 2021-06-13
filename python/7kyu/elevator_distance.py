from typing import List


def elevator_distance(array: List[int]) -> int:
    """Kata url: https://www.codewars.com/kata/59f061773e532d0c87000d16."""
    return sum(abs(new - previous) for previous, new in zip(array, array[1:]))
