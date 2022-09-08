"""Kata url: https://www.codewars.com/kata/5708f682c69b48047b000e07."""


def multiply(n):
    return (5 ** (len(str(n)) - (str(n)[0] == '-'))) * n


def test_multiply():
    assert multiply(10) == 250
    assert multiply(5) == 25
    assert multiply(200) == 25000
    assert multiply(0) == 0
    assert multiply(-2) == -10
