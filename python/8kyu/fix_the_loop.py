"""Kata url: https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd."""
from typing import List


def list_animals(animals: List[str]) -> str:
    return '\n'.join(
        f'{c + 1}. {item}' for (c, item) in enumerate(animals)
    ) + '\n'
