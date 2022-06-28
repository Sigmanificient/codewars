"""Kata url: https://www.codewars.com/kata/55ad04714f0b468e8200001c."""


def get_char(c: int) -> str:
    return chr(c)


def test_get_char():
    assert get_char(65) == 'A'
    assert get_char(97) == 'a'
    assert get_char(66) == 'B'
    assert get_char(98) == 'b'
