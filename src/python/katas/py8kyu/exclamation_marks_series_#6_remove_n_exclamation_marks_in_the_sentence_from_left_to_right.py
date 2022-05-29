"""Kata url: https://www.codewars.com/kata/57faf7275c991027af000679."""
from typing import List


def remove(s: str, n: int) -> str:
    r: List[str] = []

    for char in s:
        if char == '!' and n:
            n -= 1
            continue

        r.append(char)
    return ''.join(r)
