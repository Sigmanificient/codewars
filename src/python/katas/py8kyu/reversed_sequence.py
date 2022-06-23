"""Kata url: https://www.codewars.com/kata/5a00e05cc374cb34d100000d."""

from typing import List


def reverse_seq(n) -> List[int]:
    return list(range(n, 0, -1))


def test_reverse_seq():
    assert reverse_seq(0) == []
    assert reverse_seq(5) == [5, 4, 3, 2, 1]
    assert reverse_seq(10) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
