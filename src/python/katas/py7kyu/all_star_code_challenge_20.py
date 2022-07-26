"""Kata url: https://www.codewars.com/kata/5865a75da5f19147370000c7."""
from typing import List, TypeVar

import pytest

Addable = TypeVar("Addable", str, int)


def add_arrays(array: List[Addable], array2: List[Addable]) -> List[Addable]:
    if len(array) != len(array2):
        raise ValueError

    return [a + b for a, b in zip(array, array2)]


def test_add_arrays():
    assert add_arrays([1, 2], [4, 5]) == [5, 7]
    assert add_arrays(["a"], ["b"]) == ["ab"]

    with pytest.raises(ValueError):
        add_arrays([1, 2, 3], [4, 5])
