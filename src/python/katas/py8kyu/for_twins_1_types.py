"""Kata url: https://www.codewars.com/kata/59c1302ecb7fb48757000013."""
from typing import Any


def type_validation(variable: Any, _type: str) -> bool:
    return variable.__class__.__name__ == _type


def test_type_validation():
    assert type_validation(42, "int")
    assert not type_validation("42", "int")
