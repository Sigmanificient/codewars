"""Kata url: https://www.codewars.com/kata/563f879ecbb8fcab31000041."""

from typing import Callable, List


def factory(n: int) -> Callable[[List[int]], List[int]]:
    return lambda x: [i * n for i in x]


def test_factory():
    arr = [1, 2, 3]
    assert factory(3)(arr) == [3, 6, 9]
    assert factory(5)(arr) == [5, 10, 15]
