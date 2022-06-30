"""Kata url: https://www.codewars.com/kata/571d42206414b103dc0006a1."""

from typing import List


def arr(n: int = 0) -> List[int]:
    return list(range(n))


def test_arr():
    assert arr() == []
    assert arr(0) == []
    assert arr(-1) == []
    assert arr(4) == [0, 1, 2, 3]
    assert arr(5) == [0, 1, 2, 3, 4]
