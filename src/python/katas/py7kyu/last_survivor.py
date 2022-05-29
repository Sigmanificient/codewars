"""Kata url: https://www.codewars.com/kata/609eee71109f860006c377d1."""

from typing import List


def last_survivor(letters: str, coords: List[int]) -> str:
    buf_letters = list(letters)

    for r in coords:
        buf_letters.pop(r)

    return buf_letters[-1]
