"""Kata url: https://www.codewars.com/kata/5817030088ca96c0b7000083."""

from string import ascii_uppercase, ascii_lowercase, digits
from collections import Counter

SORT_PRIORITY = ascii_uppercase + ascii_lowercase + digits


def find_characters(matrix):
    counts = Counter(''.join(matrix.splitlines()))
    return ''.join(
        sorted((
            c for c, count in counts.items()
            if count == min(counts.values())
            ), key=SORT_PRIORITY.index
        )
    )