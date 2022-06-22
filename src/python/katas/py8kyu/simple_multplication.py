"""Kata url: https://www.codewars.com/kata/583710ccaa6717322c000105."""


def simple_multiplication(number: int) -> int:
    return number * (8 + number % 2)


def test_simple_multiplication():
    assert simple_multiplication(2) == 16
    assert simple_multiplication(1) == 9
    assert simple_multiplication(8) == 64
    assert simple_multiplication(4) == 32
    assert simple_multiplication(5) == 45
