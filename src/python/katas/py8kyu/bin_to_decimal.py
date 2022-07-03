"""Kata url: https://www.codewars.com/kata/57a5c31ce298a7e6b7000334."""


def bin_to_decimal(inp: str) -> int:
    return int(inp, 2)


def test_bin_to_decimal():
    assert bin_to_decimal("0") == 0
    assert bin_to_decimal("1") == 1
    assert bin_to_decimal("10") == 2
    assert bin_to_decimal("11") == 3
    assert bin_to_decimal("101010") == 42
    assert bin_to_decimal("1001001") == 73
