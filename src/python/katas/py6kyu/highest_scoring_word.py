"""Kata url: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272."""


def high(x: str) -> str:
    return max(x.split(" "), key=lambda v: sum(ord(y) - 96 for y in v))


def test_high():
    assert high("man i need a taxi up to ubud") == "taxi"
    assert high("what time are we climbing up the volcano") == "volcano"
    assert high("take me to semynak") == "semynak"
    assert high("aa b") == "aa"
    assert high("b aa") == "b"
    assert high("bb d") == "bb"
    assert high("d bb") == "d"
    assert high("aaa b") == "aaa"
