"""Kata url: https://www.codewars.com/kata/56cd44e1aa4ac7879200010b."""


def is_uppercase(inp: str) -> bool:
    return inp.isupper()


def test_is_uppercase():
    assert not is_uppercase("c")
    assert is_uppercase("C")
    assert not is_uppercase("hello I AM DONALD")
    assert is_uppercase("HELLO I AM DONALD")
    assert is_uppercase("$%&")