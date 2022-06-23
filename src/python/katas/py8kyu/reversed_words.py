"""Kata url: https://www.codewars.com/kata/51c8991dee245d7ddf00000e."""


def reverse_words(s: str) -> str:
    return ' '.join(s.split()[::-1])


def test_reverse_words():
    assert reverse_words('Hello World') == 'World Hello'
    assert reverse_words('Hi There.') == 'There. Hi'
