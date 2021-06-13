from typing import List


def elevator_distance(array: List[int]) -> int:
    return sum(abs(new - previous) for previous, new in zip(array, array[1:]))
