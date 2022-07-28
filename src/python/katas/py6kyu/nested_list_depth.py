"""Kata url: https://www.codewars.com/kata/56b3b9c7a6df24cf8c00000e."""
from typing import List, Union


RecursiveList = List[Union[bool, str, int, "RecursiveList"]]


def list_depth(lst: RecursiveList, d: int = 0) -> int:
    if not isinstance(lst, list):
        return d

    return max(list_depth(item, d + 1) for item in lst) if lst else d + 1


def test_list_depth():
    assert list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1]) == 6
    assert list_depth([True]) == 1
    assert list_depth([]) == 1
    assert list_depth([2, "yes", [True, False]]) == 2
    assert list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]]) == 2
    assert list_depth([[[[]]], [[[]]]]) == 4
    assert list_depth([True, False, True, [False], True]) == 2
    assert list_depth([[], [], [[], []]]) == 3
    assert list_depth([77]) == 1
    assert list_depth([2, "yes", [True, [False]]]) == 3
    assert list_depth([77, [77]]) == 2
    assert list_depth([[77], 77, [[77]]]) == 3
