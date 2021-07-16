from typing import List


def move_zeros(array: List[int]) -> List[int]:
    """Kata: https://www.codewars.com/kata/52597aa56021e91c93000cb0."""
    filtered: List[int] = list(map(bool, array))
    return filtered + [0] * (len(array) - len(filtered))
