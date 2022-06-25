"""Kata url: https://www.codewars.com/kata/57cc40b2f8392dbf2a0003ce."""

from typing import Any, List


def check(a: List[Any], x: Any) -> bool:
    return x in a


def test_check():
    assert check([66, 101], 66)
    assert check([80, 117, 115, 104, 45, 85, 112, 115], 45)
    assert check(['t', 'e', 's', 't'], 'e')
    assert not check(['what', 'a', 'great', 'kata'], 'kat')
