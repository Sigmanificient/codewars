"""Kata url: https://www.codewars.com/kata/5314b3c6bb244a48ab00076c."""
import pytest


def luck_check(string: str) -> bool:
    x = tuple(map(int, string))
    h = len(string) // 2
    return sum(x[:h]) == sum(x[::-1][:h])


def test_luck_check():
    assert luck_check("683179")
    assert not luck_check("683000")

    with pytest.raises(ValueError):
        luck_check("6F43E8")
