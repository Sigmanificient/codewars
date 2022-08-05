"""Kata url: https://www.codewars.com/kata/553e8b195b853c6db4000048."""


def has_unique_chars(string: str) -> bool:
    return len(string) == len(set(string))


def test_has_unique_chars():
    assert has_unique_chars("")
    assert not has_unique_chars("  nAa")
    assert has_unique_chars("abcdef")
    assert not has_unique_chars("++-")
