"""Kata url: https://www.codewars.com/kata/5680781b6b7c2be860000036."""

from typing import List


def vowel_indices(word: str) -> List[int]:
    return [
        c for c, l in enumerate(word, start=1)
        if l.lower() in 'aeiouy'
    ]


def test_vowel_indices():
    assert vowel_indices("mmm") == []
    assert vowel_indices("apple") == [1, 5]
    assert vowel_indices("123456") == []
    assert vowel_indices("UNDISARMED") == [1, 4, 6, 9]
