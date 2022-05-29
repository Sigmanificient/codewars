"""Kata url: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1."""


def duplicate_count(text: str) -> int:
    text = text.lower()
    return sum(True for x in set(text) if text.count(x) > 1)


def test_duplicate_count():
    assert duplicate_count("") == 0
    assert duplicate_count("abcde") == 0
    assert duplicate_count("abcdeaa") == 1
    assert duplicate_count("abcdeaB") == 2
    assert duplicate_count("Indivisibilities") == 2
