"""Kata url: https://www.codewars.com/kata/59cd155d1a68b70f8e000117."""


def middle_me(n: int, x: str, y: str) -> str:
    return x if n % 2 else x.center(n + 1, y)


def test_middle_me():
    assert middle_me(3, "a", "b") == "a"
    assert middle_me(5, "x", "y") == "x"

    assert middle_me(8, "a", "b") == "bbbbabbbb"
    assert middle_me(6, "x", "y") == "yyyxyyy"
