"""Kata url: https://www.codewars.com/kata/59b11f57f322e5da45000254."""


def ones_complement(binary_number: str) -> str:
    return ''.join('01'[c == '0'] for c in binary_number)


def test_ones_complement():
    assert ones_complement("0"), "1"
    assert ones_complement("1"), "0"
    assert ones_complement("01"), "10"
    assert ones_complement("10"), "01"
    assert ones_complement("1101"), "0010"
