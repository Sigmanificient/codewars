"""Kata url: https://www.codewars.com/kata/567bed99ee3451292c000025."""
import re


def is_vowel(s):
    return re.fullmatch('[aeiou]', s.lower()) is not None


def test_is_vowel():
    assert is_vowel("a")
    assert is_vowel("E")
    assert not is_vowel("")
    assert not is_vowel("ou")
    assert not is_vowel("z")
    assert not is_vowel("lol")
