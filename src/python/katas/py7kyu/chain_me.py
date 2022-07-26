"""Kata url: https://www.codewars.com/kata/54fb853b2c8785dd5e000957."""
from typing import Callable


def chain(init_val: int, functions: Callable[[int], int]) -> int:
    for f in functions:
        init_val = f(init_val)

    return init_val


def test_chain():
    def add10(x):
        return x + 10

    def mul30(x):
        return x * 30

    assert chain(42, []) == 42
    assert chain(50, [mul30]) == 1500
    assert chain(50, [mul30, add10]) == 1510
    assert chain(50, [add10, mul30]) == 1800
    assert chain(0, [add10] * 10) == 100
