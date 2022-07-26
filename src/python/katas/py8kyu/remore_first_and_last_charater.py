"""Kata url: https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0."""


def remove_char(s: str) -> str:
    return s[1:-1]


def test_remove_char():
    assert remove_char("ok") == ""
    assert remove_char("ooopsss") == "oopss"
    assert remove_char("eloquent") == "loquen"
    assert remove_char("country") == "ountr"
    assert remove_char("person") == "erso"
    assert remove_char("place") == "lac"
