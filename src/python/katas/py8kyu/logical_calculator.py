"""Kata url: https://www.codewars.com/kata/57096af70dad013aa200007b."""

from functools import reduce
from typing import List


def logical_calc(array: List[bool], op: str) -> bool:
    if op == "AND":
        return all(array)

    if op == "OR":
        return any(array)

    return reduce(lambda x, y: x ^ y, array)


def test_logical_calc():
    assert not logical_calc([True, False], "AND")
    assert logical_calc([True, False], "OR")
    assert logical_calc([True, False], "XOR")

    assert logical_calc([True, True, False], "OR")
    assert not logical_calc([True, True, False], "AND")
    assert not logical_calc([True, True, False], "XOR")
