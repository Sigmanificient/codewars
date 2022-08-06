"""Kata url: https://www.codewars.com/kata/57a04da9e298a7ee43000111."""
from typing import List, Any


def reverse_list(lst: List[Any]) -> List[Any]:
    return lst[::-1]


def test_reverse_list():
    assert reverse_list([]) == []
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_list([2, 4, 5, 6]) == [6, 5, 4, 2]
