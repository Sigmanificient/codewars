"""Kata url: https://www.codewars.com/kata/56200d610758762fb0000002."""


def add_five(num: int) -> int:
    return num + 5


def test_add_five():
    assert add_five(5) == 10
    assert add_five(0) == 5
    assert add_five(-5) == 0
