"""Kata url: https://www.codewars.com/kata/57a386117cb1f31890000039."""


from typing import Optional, Union


def parse_float(string: Union[list, str]) -> Optional[float]:
    if isinstance(string, list):
        return None

    if "." not in string:
        return None

    int_part, dec_part, *left_over = string.split(".")

    if left_over:
        return None

    if int_part.isdigit() and dec_part.isdigit():
        return float(string)

    return None


def _float_eq(
    left: float | None,
    right: float | None,
    threshold = 0.001
) -> bool:
    if left is None or right is None:
        return False

    return abs(left - right) < threshold


def test_parse_float():
    assert parse_float([]) is None
    assert parse_float("a") is None
    assert parse_float("1.b") is None
    assert parse_float("1.2.3") is None

    assert _float_eq(parse_float("1.0"), 1.0)
    assert _float_eq(parse_float("234.0234"), 234.0234)
    assert _float_eq(parse_float("1.234"), 1.234)