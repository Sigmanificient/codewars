"""Kata url: https://www.codewars.com/kata/5b6b128783d648c4c4000129."""
from typing import List


def mul(x: List[int]) -> int:
    result: int = 1
    for n in x:
        result *= n

    return result


def smallest_product(a: List[List[int]]) -> int:
    return min(mul(x) for x in a)
