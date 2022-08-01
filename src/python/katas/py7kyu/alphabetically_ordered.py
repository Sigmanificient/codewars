"""Kata url: https://www.codewars.com/kata/5a8059b1fd577709860000f6."""


def alphabetic(s: str) -> bool:
    return s == ''.join(sorted(s))


def test_alphabetic():
    assert not alphabetic('asd')
    assert not alphabetic('codewars')
    assert alphabetic('door')
    assert alphabetic('cell')
    assert alphabetic('z')
    assert alphabetic('')
