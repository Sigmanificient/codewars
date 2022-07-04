"""Kata url: https://www.codewars.com/kata/54ff3102c1bad923760001f3."""


def get_count(sentence: str) -> int:
    return sum(sentence.count(v) for v in "aeiou")


def test_get_count():
    assert get_count("") == 0
    assert get_count("y") == 0
    assert get_count("aeiou") == 5
    assert get_count("bcdfghjklmnpqrstvwxz y") == 0
    assert get_count("abracadabra") == 5
