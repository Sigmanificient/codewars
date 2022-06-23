"""Kata url: https://www.codewars.com/kata/57a55c8b72292d057b000594."""


def reverse(st: str) -> str:
    return ' '.join(reversed(st.split()))


def test_reverse():
    assert reverse('Hello World') == 'World Hello'
    assert reverse('Hi There.') == 'There. Hi'
