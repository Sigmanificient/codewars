"""Kata url: https://www.codewars.com/kata/557af9418895e44de7000053."""

from typing import Optional


def repeat_it(string: Optional[str], n: int) -> str:
    return string * n if isinstance(string, str) else "Not a string"


def test_repeat_it():
    assert repeat_it("*", 3) == "***"
    assert repeat_it("Hello", 5) == "HelloHelloHelloHelloHello"
