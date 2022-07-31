"""Kata url: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd."""

from typing import List, Any


def filter_list(collection: List[Any]) -> List[int]:
    return [x for x in collection if isinstance(x, int)]


def test_filter_list():
    assert filter_list([1, 2, "a", "b"]) == [1, 2]
    assert filter_list([1, "a", "b", 0, 15]) == [1, 0, 15]
    assert filter_list([1, 2, "aasf", "1", "123", 123]) == [1, 2, 123]
    assert filter_list([]) == []
