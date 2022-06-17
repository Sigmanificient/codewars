"""Kata url: https://www.codewars.com/kata/5547929140907378f9000039."""


def shortcut(s: str) -> str:
    return ''.join(x for x in s if x not in 'aeiou')


def test_shortcut():
    assert shortcut("") == ""
    assert shortcut("aeiou") == ""
    assert shortcut("abc") == "bc"
    assert shortcut("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"
