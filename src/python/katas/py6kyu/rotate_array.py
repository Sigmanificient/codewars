"""Kata url: https://www.codewars.com/kata/5469e0798a3502f4a90005c9."""
from typing import Any, List


def rotate(data: List[Any], n: int) -> List[Any]:
    if not data:
        return []

    n %= len(data)
    return data[-n:] + data[:-n]


def test_rotate():
    assert rotate([], 976999) == []
    assert rotate([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
    assert rotate([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1]
    assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]
    assert rotate([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
    assert rotate([1, 2, 3, 4, 5], -3) == [4, 5, 1, 2, 3]
    assert rotate([1, 2, 3, 4, 5], 4) == [2, 3, 4, 5, 1]
    assert rotate([1, 2, 3, 4, 5], -4) == [5, 1, 2, 3, 4]
    assert rotate([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert rotate([1, 2, 3, 4, 5], -5) == [1, 2, 3, 4, 5]
    assert rotate([1, 2, 3, 4, 5], 6) == [5, 1, 2, 3, 4]
    assert rotate([1, 2, 3, 4, 5], -6) == [2, 3, 4, 5, 1]
    assert rotate([True, True, False], 2) == [True, False, True]
    assert rotate([1, 2, 3, 4, 5], 12478) == [3, 4, 5, 1, 2]
    assert rotate(['a', 'b', 'c'], 2) == ['b', 'c', 'a']
