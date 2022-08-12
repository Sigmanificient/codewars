"""Kata url: https://www.codewars.com/kata/585b1fafe08bae9988000314."""


def explode(s: str) -> str:
    return ''.join(c * int(c) for c in s)


def test_explode():
    assert explode("312") == "333122"
    assert explode("102269") == "12222666666999999999"
    assert explode("0") == ""
    assert explode("000") == ""
    assert explode("123") == "122333"
