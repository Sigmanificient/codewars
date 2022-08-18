"""Kata url: https://www.codewars.com/kata/5963c18ecb97be020b0000a2."""


def derive(a: int, b: int) -> str:
    return f"{a * b}x^{b - 1}"


def test_derive():
    assert derive(7, 8) == "56x^7"
    assert derive(5, 9) == "45x^8"
    assert derive(3, 2) == "6x^1"
    assert derive(10, 10) == "100x^9"
