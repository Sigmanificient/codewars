"""Kata url: https://www.codewars.com/kata/551f37452ff852b7bd000139."""


def add_binary(a: int, b: int) -> str:
    return f"{a + b:b}"


def test_add_binary():
    assert add_binary(1, 1) == "10"
    assert add_binary(0, 1) == "1"
    assert add_binary(1, 0) == "1"
    assert add_binary(2, 2) == "100"
    assert add_binary(51, 12) == "111111"
