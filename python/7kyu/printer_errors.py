"""Kata url: https://www.codewars.com/kata/56541980fa08ab47a0000040."""


def printer_errors(s: str) -> str:
    return f"{sum(c not in 'abcdefghijklm' for c in s)}/{len(s)}"
