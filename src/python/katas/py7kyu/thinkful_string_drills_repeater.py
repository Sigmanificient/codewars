"""Kata url: https://www.codewars.com/kata/585a1a227cb58d8d740001c3."""


def repeater(string: str, n: int) -> str:
    return string * n


def test_repeater():
    assert repeater('a', 5) == 'aaaaa'
    assert repeater('Na', 16) == 'NaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNa'
    assert repeater('Wub ', 6) == 'Wub Wub Wub Wub Wub Wub '
