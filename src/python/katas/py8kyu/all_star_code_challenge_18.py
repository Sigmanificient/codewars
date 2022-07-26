"""Kata url: https://www.codewars.com/kata/5865918c6b569962950002a1."""


def str_count(string: str, letter: str) -> int:
    return string.count(letter)


def test_str_count():
    assert str_count("hello", "l") == 2
    assert str_count("hello", "e") == 1
    assert str_count("codewars", "c") == 1
    assert str_count("ggggg", "g") == 5
    assert str_count("hello world", "o") == 2
    assert str_count("", "z") == 0
