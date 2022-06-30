"""Kata url: https://www.codewars.com/kata/57faece99610ced690000165."""


def remove(s: str) -> str:
    if not s.endswith('!'):
        return s

    for c, char in enumerate(s[::-1]):
        if char != '!':
            return s[:-c]

    return s


def test_remove():
    assert remove("Hi!") == "Hi"
    assert remove("Hi!!!") == "Hi"
    assert remove("!Hi") == "!Hi"
    assert remove("!Hi!") == "!Hi"
    assert remove("Hi! Hi!") == "Hi! Hi"
    assert remove("Hi") == "Hi"
