"""Kata url: https://www.codewars.com/kata/56fa3c5ce4d45d2a52001b3c."""


def xor(a: bool, b: bool) -> bool:
    return a ^ b


def test_xor():
    assert xor(True, False)
    assert xor(False, True)
    assert not xor(True, True)
    assert not xor(False, False)
