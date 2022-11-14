"""Kata url: https://www.codewars.com/kata/54129112fb7c188740000162."""
from typing import Any


def prefill(n: Any, v: Any = 0):
    if isinstance(n, float) or n is None:
        raise TypeError(f"{n} is invalid")
    if isinstance(n, str) and not n.isdigit():
        raise TypeError(f"{n} is invalid")
    return [v] * int(n)


def test_prefill():
    assert prefill(3, 1) == [1, 1, 1]
    assert prefill(2, 'abc') == ['abc', 'abc']
    assert prefill('1', 1) == [1]
    assert prefill(3, prefill(2, '2d')) == [
        ['2d', '2d'], ['2d', '2d'], ['2d', '2d']
    ]
