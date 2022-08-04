"""Kata url: https://www.codewars.com/kata/580dda86c40fa6c45f00028a."""
from typing import List, Union


def cube_odd(arr: List[Union[int, bool, str]]) -> int:
    total = 0
    for i in arr:
        if type(i) != int:
            return

        if i % 2:
            total += i ** 3

    return total


def test_cube_odd():
    assert cube_odd([1, 2, 3, 4]) == 28
    assert cube_odd([-3, -2, 2, 3]) == 0
    assert cube_odd(["a", 12, 9, "z", 42]) is None
    assert cube_odd([True, False, 2, 4, 1]) is None
