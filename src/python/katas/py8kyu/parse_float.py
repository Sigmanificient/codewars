"""Kata url: https://www.codewars.com/kata/57a386117cb1f31890000039."""


from typing import Optional


def parse_float(string: str) -> Optional[float]:
    if isinstance(string, list):
        return None

    if '.' not in string:
        return None

    int_part, dec_part = string.split('.')
    if int_part.isdigit() and dec_part.isdigit():
        return float(string)

    return None


def test_parse_float():
    assert parse_float([]) is None
    assert parse_float("a") is None
    assert parse_float("1.b") is None
    assert parse_float("1.2.3") is None

    assert parse_float("1.0") == 1.0
    assert parse_float("234.0234") == 234.0234
    assert parse_float("1.234") == 1.234
