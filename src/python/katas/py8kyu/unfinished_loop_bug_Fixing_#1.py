"""Kata url: https://www.codewars.com/kata/55c28f7304e3eaebef0000da."""

from typing import List


def create_array(n: int) -> List[int]:
    return list(range(1, n + 1))


def test_create_array():
    assert create_array(1) == [1]
    assert create_array(2) == [1, 2]
    assert create_array(3) == [1, 2, 3]
    assert create_array(4) == [1, 2, 3, 4]
    assert create_array(5) == [1, 2, 3, 4, 5]
    assert create_array(6) == [1, 2, 3, 4, 5, 6]
    assert create_array(7) == [1, 2, 3, 4, 5, 6, 7]
    assert create_array(8) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert create_array(9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert create_array(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]