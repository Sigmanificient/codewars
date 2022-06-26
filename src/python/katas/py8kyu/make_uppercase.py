"""Kata url: https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7."""


def make_upper_case(s: str) -> str:
    return s.upper()


def test_make_upper_case():
    assert make_upper_case("hello") == "HELLO"
    assert make_upper_case("world") == "WORLD"
    assert make_upper_case("hello world") == "HELLO WORLD"
    assert make_upper_case("") == ""
