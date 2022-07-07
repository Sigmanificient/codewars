"""Kata url: https://www.codewars.com/kata/574b1916a3ebd6e4fa0012e7."""


def is_opposite(s1: str, s2: str) -> bool:
    return bool(len(s1)) and s1 == s2.swapcase()


def test_is_opposite():
    assert is_opposite("ab", "AB")
    assert is_opposite("aB", "Ab")
    assert is_opposite("aBcd", "AbCD")
    assert not is_opposite("AB", "Ab")
    assert not is_opposite("", "")
