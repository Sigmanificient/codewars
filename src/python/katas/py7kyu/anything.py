"""Kata url: https://www.codewars.com/kata/557d9e4d155e2dbf050000aa."""
from typing import Any


class Anything:
    @staticmethod
    def _any(_other: Any) -> bool:
        return True

    __gt__ = __lt__ = __ge__ = __le__ = __eq__ = __ne__ = _any


def anything(_thing: Any) -> Anything:
    return Anything()


def test_anything():
    assert anything({}) != []
    assert anything('Hello') < 'World'
    assert anything(80) > 81

    import re
    assert anything(re) >= re

    import math
    assert anything(re) <= math

    assert anything(5) == ord

    for i in range(5):
        assert anything(i) == i
        assert anything(i) == -i
        assert anything(i) == f"{str(-i)} {str(i)}"

    assert anything({}) == []
