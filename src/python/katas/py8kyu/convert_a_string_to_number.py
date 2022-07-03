"""Kata url: https://www.codewars.com/kata/544675c6f971f7399a000e79."""


def string_to_number(s: str) -> int:
    return int(s)


def test_string_to_number():
    assert string_to_number("-7") == -7
    assert string_to_number("1234") == 1234
    assert string_to_number("605") == 605
    assert string_to_number("1405") == 1405
