"""Kata url: https://www.codewars.com/kata/57096af70dad013aa200007b."""

from functools import reduce
from typing import List


def logical_calc(array: List[bool], op: str) -> bool:
    if op == "AND":
        return all(array)

    if op == "OR":
        return any(array)

    return reduce(lambda x, y: x ^ y, array)
