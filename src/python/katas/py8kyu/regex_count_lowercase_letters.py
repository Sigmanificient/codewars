"""Kata url: https://www.codewars.com/kata/56a946cd7bd95ccab2000055."""


def lowercase_count(string: str) -> int:
    return sum(x.islower() for x in string)


def test_lowercase_count():
    assert lowercase_count("") == 0
    assert lowercase_count("abc") == 3
    assert lowercase_count("abcABC123") == 3
    assert lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~") == 3
    assert lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~") == 0
    assert lowercase_count("abcdefghijklmnopqrstuvwxyz") == 26
