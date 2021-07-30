"""Kata url: https://www.codewars.com/kata/609eee71109f860006c377d1."""

from typing import List


def last_survivor(letters: str, coords: List[int, int]) -> str:
    letters: List[str] = list(letters)

    for r in coords:
        letters.pop(r)

    return letters[-1]
