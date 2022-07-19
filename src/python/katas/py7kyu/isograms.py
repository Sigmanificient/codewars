"""Kata url: https://www.codewars.com/kata/54ba84be607a92aa900000f1."""


def is_isogram(string: str) -> bool:
    return len(string) == len(set(string.lower()))


def test_isogram():
    assert is_isogram("")
    assert is_isogram("Dermatoglyphics")
    assert is_isogram("isogram")
    assert not is_isogram("aba")
    assert not is_isogram("moOse")
    assert not is_isogram("isIsogram")
