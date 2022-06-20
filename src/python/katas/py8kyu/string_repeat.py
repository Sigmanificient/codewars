"""Kata url: https://www.codewars.com/kata/57a0e5c372292dd76d000d7e."""


def repeat_str(repeat: int, string: str) -> str:
    return string * repeat


def test_repeat_str():
    assert repeat_str(4, 'a') == 'aaaa'
    assert repeat_str(3, 'hello ') == 'hello hello hello '
    assert repeat_str(2, 'abc') == 'abcabc'
