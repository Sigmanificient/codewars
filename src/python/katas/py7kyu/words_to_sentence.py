"""Kata url: https://www.codewars.com/kata/57a06005cf1fa5fbd5000216."""

from typing import List


def words_to_sentence(words: List[str]) -> str:
    return ' '.join(words)


def test_words_to_sentence():
    assert words_to_sentence(['bacon', 'is', 'delicious']) == 'bacon is delicious'
    assert words_to_sentence(['hello', 'world']) == 'hello world'
