"""Kata url: https://www.codewars.com/kata/56541980fa08ab47a0000040."""


def printer_errors(s: str) -> str:
    return f'{sum(1 for c in s if c not in "abcdefghijklm")}/{len(s)}'
