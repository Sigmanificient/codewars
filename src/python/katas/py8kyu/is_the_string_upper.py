"""Kata url: https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train."""


def is_uppercase(inp: str) -> bool:
    return inp.isupper()


def test_is_uppercase():
    assert not is_uppercase("c")
    assert "C"
    assert not is_uppercase("hello I AM DONALD")
    assert "HELLO I AM DONALD"
    assert "$%&"
