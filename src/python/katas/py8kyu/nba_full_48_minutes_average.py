"""Kata url: https://www.codewars.com/kata/587c2d08bb65b5e8040004fd."""


def nba_extrap(ppg: int | float, mpg: int | float) -> int | float:
    return round((ppg / mpg) * 48, 1) or 0


def _float_eq(
    left: float | int,
    right: float | int,
    threshold = 0.001
) -> bool:
    return abs(left - right) < threshold


def test_nba_extrap():
    assert _float_eq(nba_extrap(0, 0), 0)
    assert _float_eq(nba_extrap(12, 20), 28.8)
    assert _float_eq(nba_extrap(10, 10), 48.0)
    assert _float_eq(nba_extrap(5, 17), 14.1)
    assert _float_eq(nba_extrap(30.8, 34.7), 42.6)
    assert _float_eq(nba_extrap(22.9, 33.8), 32.5)