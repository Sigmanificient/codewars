"""Kata url: https://www.codewars.com/kata/56676e8fabd2d1ff3000000c."""

from typing import List


def find_needle(haystack: List[str]) -> str:
    return f"found the needle at position {haystack.index('needle')}"
