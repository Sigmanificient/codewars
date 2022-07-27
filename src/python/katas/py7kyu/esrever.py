"""Kata url: https://www.codewars.com/kata/5413759479ba273f8100003d."""
from typing import Any, List


def reverse(lst: List[Any]) -> List[Any]:
    rev = list()  # sourcery skip: list-literal
    while lst:
        rev.append(lst.pop())
    return rev


def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert reverse([1, None, 14, "two"]) == ["two", 14, None, 1]
    assert reverse([0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
    assert reverse([]) == []
