"""Kata url: https://www.codewars.com/kata/56a25ba95df27b7743000016."""

import re


def validate_code(code: int) -> bool:
    return bool(re.match(r'[1-3].*', str(code)))


def test_validate_code():
    assert validate_code(123)
    assert validate_code(248)
    assert not validate_code(8)
    assert validate_code(321)
    assert not validate_code(9453)
