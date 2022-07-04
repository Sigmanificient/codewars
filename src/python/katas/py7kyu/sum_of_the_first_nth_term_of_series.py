"""Kata url: https://www.codewars.com/kata/555eded1ad94b00403000071."""


def series_sum(n: int) -> str:
    return f"{sum(1/(1 + 3 * x) for x in range(n)):.2f}"


def test_series():
    assert series_sum(1) == "1.00"
    assert series_sum(2) == "1.25"
    assert series_sum(3) == "1.39"
