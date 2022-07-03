"""Kata url: https://www.codewars.com/kata/5265326f5fda8eb1160004c8."""


def number_to_string(num: int) -> str:
    return str(num)


def test_number_to_string():
    assert number_to_string(1 - 2) == '-1'
    assert number_to_string(67) == '67'
    assert number_to_string(79585) == '79585'
    assert number_to_string(79585) == "79585"
    assert number_to_string(1 + 2) == '3'
    assert number_to_string(0) == '0'
