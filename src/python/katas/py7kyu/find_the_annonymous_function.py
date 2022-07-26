"""Kata url: https://www.codewars.com/kata/55a12bb8f0fac1ba340000aa."""
from typing import List, Union, Callable


def find_function(func: List[Union[int, Callable[[int], bool]]], arr: List[int]):
    return list(filter(max(func, key=callable), arr))


def test_find_function():
    assert find_function([lambda a: a % 2 == 0, 9, 3, 1, 0], [1, 2, 3, 4]) == [2, 4]
    assert find_function([9, 3, lambda a: a % 2, 1, 0], [1, 2, 3, 4]) == [1, 3]
    assert find_function([9, 3, lambda a: a % 13 == 0, 1, 0], [1, 2, 3, 4]) == []
    assert find_function([9, 3, lambda a: a % 13 != 0, 1, 0], [1, 2, 3, 4]) == [
        1,
        2,
        3,
        4,
    ]
    assert find_function([5, 1, lambda a: a != 0, 1, 0], [0, 1, 2, 3, 4]) == [
        1,
        2,
        3,
        4,
    ]
