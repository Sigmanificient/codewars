"""Kata url: https://www.codewars.com/kata/5546180ca783b6d2d5000062."""
from typing import List


def squares(x: int, n: int) -> List[int]:
    return [(x := x ** 2) if c else x for c in range(n)]


def test_squares():
    assert squares(2, 5) == [2, 4, 16, 256, 65536]
    assert squares(3, 3) == [3, 9, 81]
    assert squares(5, 3) == [5, 25, 625]
    assert squares(10, 4) == [10, 100, 10000, 100000000]
    assert squares(2, 0) == []
    assert squares(2, -4) == []
