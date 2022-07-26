"""Kata url: https://www.codewars.com/kata/5c707567c447bd46c6bafd68."""


def usd(eur: int) -> str:
    return f"${eur * 1.1363636:.2f}"


def test_usd():
    assert usd(1) == "$1.14"
    assert usd(2) == "$2.27"
    assert usd(5) == "$5.68"
    assert usd(20) == "$22.73"
    assert usd(50) == "$56.82"
