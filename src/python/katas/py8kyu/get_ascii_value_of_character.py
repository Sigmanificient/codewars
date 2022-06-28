"""Kata url: https://www.codewars.com/kata/55acfc59c3c23d230f00006d."""


def get_ascii(c: str) -> int:
    return ord(c)


def test_get_ascii():
    assert get_ascii("A") == 65
    assert get_ascii(" ") == 32
    assert get_ascii("!") == 33
