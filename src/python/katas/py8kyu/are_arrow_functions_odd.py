"""Kata url: https://www.codewars.com/kata/559f80b87fa8512e3e0000f5."""

from typing import Callable, List

odds: Callable[[List[int]], List[int]] = lambda arr: [x for x in arr if x % 2]


def test_solution():
    assert odds([]) == []
    assert odds([2, 4, 6]) == []
    assert odds([1, 3, 5]) == [1, 3, 5]
    assert odds([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
