"""Kata url: https://www.codewars.com/kata/582cb0224e56e068d800003c."""


def litres(time: float) -> float:
    return time // 2


def test_litres():
    assert litres(2) == 1
    assert litres(1.4) == 0
    assert litres(12.3) == 6
    assert litres(0.82) == 0
    assert litres(11.8) == 5
    assert litres(1787) == 893
    assert litres(0) == 0
