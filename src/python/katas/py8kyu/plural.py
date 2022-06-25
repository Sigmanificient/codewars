"""Kata url: https://www.codewars.com/kata/52ceafd1f235ce81aa00073a."""

from typing import Union


def plural(n: Union[float, int]) -> bool:
    return n != 1


def test_plural():
    assert plural(0)
    assert not plural(1)
    assert plural(100)
