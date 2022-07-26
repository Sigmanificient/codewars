"""Kata url: https://www.codewars.com/kata/513fa1d75e4297ba38000003."""
from typing import Any, List


def flatten(*args: List[Any]) -> List[Any]:
    out = []
    for item in args:
        if isinstance(item, list):
            out.extend(flatten(*item))

        else:
            out.append(item)

    return out


def test_flatten():
    assert flatten() == []
    assert flatten(1, 2, 3) == [1, 2, 3]
    assert flatten(1, 2) == [1, 2]
    assert flatten(5, "string") == [5, "string"]
    assert flatten(-4.5, -3, 1, 4) == [-4.5, -3, 1, 4]

    assert flatten([3, 4, 5], [1, 2, 3]) == [3, 4, 5, 1, 2, 3]
    assert flatten([1], [], 2, [4, 5, 6]) == [1, 2, 4, 5, 6]
    assert flatten([4, "string", 9, 3, 1], [], [], [], [], ["string"]) == [
        4,
        "string",
        9,
        3,
        1,
        "string",
    ]

    assert flatten(1, 2, ["9", [], []], None) == [1, 2, "9", None]
    assert flatten([1, 2], [3, 4, 5], [6, [7], [[8]]]) == [1, 2, 3, 4, 5, 6, 7, 8]
