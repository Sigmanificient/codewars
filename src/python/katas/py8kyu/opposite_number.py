"""Kata url: https://www.codewars.com/kata/56dec885c54a926dcd001095."""


def opposite(number: float) -> float:
    return -number

def _float_eq(
    left: float | int,
    right: float | int,
    threshold = 0.001
) -> bool:
    return abs(left - right) < threshold


def test_opposite():
    assert opposite(1) == -1
    assert _float_eq(opposite(25.6), -25.6)
    assert opposite(0) == 0
    assert _float_eq(opposite(1425.2222), -1425.2222)
    assert _float_eq(opposite(-3.1458), 3.1458)
    assert opposite(-95858588225) == 95858588225