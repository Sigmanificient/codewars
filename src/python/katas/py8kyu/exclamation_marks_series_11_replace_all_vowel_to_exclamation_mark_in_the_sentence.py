"""Kata url: https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed."""


def replace_exclamation(s: str) -> str:
    return ''.join(
        '!' if char.lower() in 'aeiou' else char for char in s
    )


def test_replace_exclamation():
    assert replace_exclamation("Hi!") == "H!!"
    assert replace_exclamation("!Hi! Hi!") == "!H!! H!!"
    assert replace_exclamation("aeiou") == "!!!!!"
    assert replace_exclamation("ABCDE") == "!BCD!"
