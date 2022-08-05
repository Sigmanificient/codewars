"""Kata url: https://www.codewars.com/kata/592a33e549fe9840a8000ba1."""


def is_even(n: int) -> bool:
    return n == ((n >> 1) * 2)


def test_is_even():
    assert is_even(2)
    assert not is_even(3)
    assert is_even(14)
    assert not is_even(15)
    assert is_even(26)
    assert not is_even(27)
