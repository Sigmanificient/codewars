from typing import Optional


def parse_float(string: str) -> Optional[float]:
    """Kata url: https://www.codewars.com/kata/57a386117cb1f31890000039."""
    if isinstance(string, list):
        return

    if '.' not in string:
        return

    int_part, dec_part = string.split('.')
    if int_part.isdigit() and dec_part.isdigit():
        return float(string)
