"""Kata url: https://www.codewars.com/kata/596c6eb85b0f515834000049."""


def replace_dots(string: str) -> str:
    return string.replace('.', '-')


def test_replace_dots():
    assert replace_dots("") == ""
    assert replace_dots("no dots") == "no dots"
    assert replace_dots("one.two.three") == "one-two-three"
    assert replace_dots("........") == "--------"
