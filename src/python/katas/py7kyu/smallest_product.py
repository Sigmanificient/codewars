"""Kata url: https://www.codewars.com/kata/5b6b128783d648c4c4000129."""
from typing import List


def mul(x: List[int]) -> int:
    result: int = 1
    for n in x:
        result *= n

    return result


def smallest_product(a: List[List[int]]) -> int:
    return min(mul(x) for x in a)


def test_mul():
    assert mul([1, 2, 3]) == 6
    assert mul([1, 2, 3, 4]) == 24
    assert mul([1, 2, 3, 4, 5]) == 120


def test_smallest_product():
    assert smallest_product([[3, 2], [1, 2, 1], [7, 8]]) == 2
    assert smallest_product([[10], [3, 0], [-1, -6, 2]]) == 0
