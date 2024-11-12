"""Kata url: https://www.codewars.com/kata/57a4c85de298a795210002da."""
from collections import Counter

words: list[str]


def longest_word(letters: str) -> list[str] | None:
    available = Counter(letters)
    possible_words = [
        word for word in words
        if all(
            available.get(letter, 0) >= count
            for letter, count in Counter(word).items()
        )
    ]

    if not possible_words:
        return None

    longest = len(max(possible_words, key=len))
    return [
        word for word in possible_words
        if len(word) == longest
    ]