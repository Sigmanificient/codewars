"""Kata url: https://www.codewars.com/kata/5b39e3772ae7545f650000fc."""
from typing import List


def remove_duplicate_words(s: str) -> str:
    words: List[str] = s.split()
    return " ".join(sorted(set(words), key=words.index))
