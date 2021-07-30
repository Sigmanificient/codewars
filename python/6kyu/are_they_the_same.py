"""Kata url: https://www.codewars.com/kata/550498447451fbbd7600041c."""

from typing import List, Optional


def comp(array: Optional[List[int]], array2: Optional[List[int]]) -> bool:
    if array is None or array2 is None:
        return False

    if len(array) != len(array2):
        return False

    return all(
        i * i == j for i, j in zip(sorted(array, key=abs), sorted(array2))
    )
