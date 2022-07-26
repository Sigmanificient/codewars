"""Kata url: https://www.codewars.com/kata/595970246c9b8fa0a8000086."""


def capitalize_word(word: str) -> str:
    return word.capitalize()


def test_capitalize_word():
    assert capitalize_word("word") == "Word"
    assert capitalize_word("i") == "I"
    assert capitalize_word("glasswear") == "Glasswear"
