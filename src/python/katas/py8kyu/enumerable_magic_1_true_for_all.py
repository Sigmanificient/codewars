"""Kata url: https://www.codewars.com/kata/54598d1fcbae2ae05200112c."""

from typing import Callable, Any, Sequence


def _all(seq: Sequence[Any], fun: Callable[[Any], bool]) -> bool:
    return sum(fun(x) for x in seq) == len(seq)


def test_all():
    assert not _all((1, 2, 3, 4, 5), lambda x: x > 9)
    assert _all((1, 2, 3, 4, 5), lambda x: x < 9)