"""Kata url: https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1."""


def get_age(age: str) -> int:
    return int(age[0])


def test_get_age():
    assert get_age("2 years old") == 2
    assert get_age("4 years old") == 4
    assert get_age("5 years old") == 5
    assert get_age("7 years old") == 7
