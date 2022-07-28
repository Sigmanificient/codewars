"""Kata url: https://www.codewars.com/kata/55a8a36703fe4c45ed00005b."""


def multiple(x: int) -> str:
    return "Bang" * (not x % 3) + "Boom" * (not x % 5) or "Miss"


def test_multiple():
    assert multiple(3) == "Bang"
    assert multiple(5) == "Boom"
    assert multiple(7) == "Miss"
    assert multiple(10) == "Boom"
    assert multiple(15) == "BangBoom"
