"""Kata url: https://www.codewars.com/kata/56747fd5cb988479af000028."""


def get_middle(s: str) -> str:
    length: int = len(s)
    middle: int = length // 2
    return s[middle - (not length % 2) : middle + 1]


def test_get_middle():
    assert get_middle("test") == "es"
    assert get_middle("testing") == "t"
    assert get_middle("middle") == "dd"
    assert get_middle("A") == "A"
    assert get_middle("of") == "of"
