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


def test_count_positives_sum_negatives():
    assert count_positives_sum_negatives([]) == []
    assert count_positives_sum_negatives([1]) == [1, 0]
    assert count_positives_sum_negatives([-1]) == [0, -1]
    assert count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65]
    assert count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8, -50]
    assert count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0]
