"""Kata url: https://www.codewars.com/kata/62a611067274990047f431a8."""

from typing import List, TypeVar

T1 = TypeVar('T1')
T2 = TypeVar('T2')


def alternate(n: int, a: T1, b: T2) -> List[T1 | T2]:
    return [b if c % 2 else a for c in range(n)]


def test_alternate():
    assert alternate(0, "lemons", "apples") == []
    assert alternate(5, True, False) == [True, False, True, False, True]
    assert alternate(20, "blue", "red") == [
        "blue",
        "red",
        "blue",
        "red",
        "blue",
        "red",
        "blue",
        "red",
        "blue",
        "red",
        "blue",
        "red",
        "blue",
        "red",
        "blue",
        "red",
        "blue",
        "red",
        "blue",
        "red",
    ]