"""Kata url: https://www.codewars.com/kata/5a3dd29055519e23ec000074."""

from typing import List


def check_exam(arr1: List[str], arr2: List[str]) -> int:
    return max(
        0, sum(
            (-1 if x != y else 4) if y else 0
            for x, y in zip(arr1, arr2)
        )
    )


def test_check_exam():
    assert check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"]) == 0
    assert check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) == 6
    assert check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""]) == 7
    assert check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) == 16
