"""Kata url: https://www.codewars.com/kata/57fae964d80daa229d000126."""


def remove(s: str) -> str:
    return s[:-1] if s.endswith("!") else s


def test_remove():
    assert remove("Hi!") == "Hi"
    assert remove("Hi!!!") == "Hi!!"
    assert remove("!Hi") == "!Hi"
    assert remove("!Hi!") == "!Hi"
    assert remove("Hi! Hi!") == "Hi! Hi"
    assert remove("Hi") == "Hi"
