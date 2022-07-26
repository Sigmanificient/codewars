"""Kata url: https://www.codewars.com/kata/57a0885cbb9944e24c00008e."""


def remove_exclamation_marks(s: str) -> str:
    return s.replace("!", "")


def test_remove_exclamation_marks():
    assert remove_exclamation_marks("") == ""
    assert remove_exclamation_marks("Oh, no!!!") == "Oh, no"
    assert remove_exclamation_marks("Hello World!") == "Hello World"
    assert remove_exclamation_marks("Hello World!!!") == "Hello World"
    assert remove_exclamation_marks("Hi! Hello!") == "Hi Hello"
