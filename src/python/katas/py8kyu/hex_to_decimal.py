"""Kata url: https://www.codewars.com/kata/57a4d500e298a7952100035d."""
import pytest


def hex_to_dec(s: str) -> int:
    return int(s, 16)


def test_hex_to_dec():
    assert hex_to_dec("0") == 0
    assert hex_to_dec("1") == 1
    assert hex_to_dec("a") == 10
    assert hex_to_dec("10") == 16
    assert hex_to_dec("ff") == 255
    assert hex_to_dec("F" * 4) == 65535
    assert hex_to_dec("F" * 8) == 4294967295

    with pytest.raises(ValueError):
        hex_to_dec("g")
