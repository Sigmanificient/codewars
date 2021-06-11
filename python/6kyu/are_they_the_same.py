from typing import List, Optional


def comp(array1: Optional[List[int]], array2: Optional[List[int]]) -> bool:
    """Kata url: https://www.codewars.com/kata/550498447451fbbd7600041c/train/python."""
    if array1 is None or array2 is None:
        return False

    if len(array1) != len(array2):
        return False

    return all(i * i == j for i, j in zip(sorted(array1, key=abs), sorted(array2)))
