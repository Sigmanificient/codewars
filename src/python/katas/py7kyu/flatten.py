"""Kata url: https://www.codewars.com/kata/5250a89b1625e5decd000413."""
from typing import Any, List


def flatten(lst: List[Any]) -> List[Any]:
    out = []
    for y in lst:
        if isinstance(y, list):
            out.extend(y)
        else:
            out.append(y)
    return out


def test_flatten():
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten(
        [[1, 2, 3], ["a", "b", "c"], [1, 2, 3]]
    ) == [1, 2, 3, "a", "b", "c", 1, 2, 3]
    assert flatten(
        [[1, 2, 3], ["a", "b", "c"], [1, 2, 3], "a"]
    ) == [1, 2, 3, "a", "b", "c", 1, 2, 3, "a"]
    assert flatten(
        [[3, 4, 5], [[9, 9, 9]], ["a,b,c"]]
    ) == [3, 4, 5, [9, 9, 9], "a,b,c"]
    assert flatten(
        [[[3], [4], [5]], [9], [9], [8], [[1, 2, 3]]]
    ) == [[3], [4], [5], 9, 9, 8, [1, 2, 3]]
