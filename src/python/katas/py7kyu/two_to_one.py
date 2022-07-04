"""Kata url: https://www.codewars.com/kata/5656b6906de340bd1b0000ac."""


def longest(a1: str, a2: str) -> str:
    return ''.join(sorted(set(a1 + a2)))


def test_longest():
    assert longest("aretheyhere", "yestheyarehere") == "aehrsty"
    assert longest("loopingisfunbutdangerous", "lessdangerousthancoding") == "abcdefghilnoprstu"
    assert longest("inmanylanguages", "theresapairoffunctions") == "acefghilmnoprstuy"
