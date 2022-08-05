"""Kata url: https://www.codewars.com/kata/5b39e3772ae7545f650000fc."""
from typing import List


def remove_duplicate_words(s: str) -> str:
    words: List[str] = s.split()
    return " ".join(sorted(set(words), key=words.index))


def test_remove_duplicate_words():
    assert remove_duplicate_words(
        "alpha beta beta gamma gamma gamma delta "
        "alpha beta beta gamma gamma gamma delta"
    ) == "alpha beta gamma delta"

    assert remove_duplicate_words("my cat is my cat fat") == "my cat is fat"
