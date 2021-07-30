"""Kata url: https://www.codewars.com/kata/57eae65a4321032ce000002d."""


def fake_bin(x: str) -> str:
    return ''.join('1' if int(c) >= 5 else '0' for c in x)
