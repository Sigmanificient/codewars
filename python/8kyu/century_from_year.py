"""Kata url: https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097."""

from math import ceil


def century(year: int) -> int:
    return ceil(year / 100)
