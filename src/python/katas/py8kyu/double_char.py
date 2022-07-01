"""Kata url: https://www.codewars.com/kata/56b1f01c247c01db92000076."""


def double_char(s: str) -> str:
    return ''.join(c * 2 for c in s)


def test_double_char():
    assert double_char("String") == "SSttrriinngg"
    assert double_char("Hello World") == "HHeelllloo  WWoorrlldd"
    assert double_char("1234!_ ") == "11223344!!__  "
