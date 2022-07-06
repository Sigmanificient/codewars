"""Kata url: https://www.codewars.com/kata/57faece99610ced690000165."""


def remove(s: str) -> str:
    return next(
        (s[:-c] for c, char in enumerate(s[::-1]) if char != '!'), s
    ) if s.endswith('!') else s


def test_remove():
    assert remove("Hi!") == "Hi"
    assert remove("Hi!!!") == "Hi"
    assert remove("!Hi") == "!Hi"
    assert remove("!Hi!") == "!Hi"
    assert remove("Hi! Hi!") == "Hi! Hi"
    assert remove("Hi") == "Hi"
