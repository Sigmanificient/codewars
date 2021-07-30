"""Kata url: https://www.codewars.com/kata/576bb71bbbcf0951d5000044."""

from typing import List


def count_positives_sum_negatives(arr: List[int]) -> List[int]:
    if not arr:
        return []

    r: int = 0
    c: int = 0

    for i in arr:
        if i <= 0:
            r += i

        else:
            c += 1

    return [c, r]
