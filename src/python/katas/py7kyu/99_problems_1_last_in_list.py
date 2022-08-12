"""Kata url: https://www.codewars.com/kata/57d86d3d3c3f961278000005."""
from typing import List, TypeVar, Optional

T = TypeVar('T')


def last(lst: List[T]) -> Optional[T]:
    return lst[-1] if lst else None


def test_last():
    assert last([1, 2, 3]) == 3
    assert last([]) is None
    assert last([2, 1, 0]) == 0
    assert last(["a", "b", ""]) == ""
