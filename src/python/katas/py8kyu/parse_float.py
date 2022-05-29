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
