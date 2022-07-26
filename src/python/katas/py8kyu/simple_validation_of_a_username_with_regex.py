"""Kata url: https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023."""

import re


def validate_usr(username: str) -> bool:
    return re.fullmatch(r"[a-z\d_]{4,16}", username) is not None


def test_validate_user():
    assert validate_usr("asddsa")
    assert not validate_usr("a")
    assert not validate_usr("Hass")
    assert not validate_usr("Hasd_12assssssasasasasasaasasasasas")
    assert not validate_usr("")
    assert validate_usr("____")
    assert not validate_usr("012")
    assert validate_usr("p1pp1")
    assert not validate_usr("asd43 34")
    assert validate_usr("asd43_34")
