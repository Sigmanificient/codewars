"""Kata url: https://www.codewars.com/kata/563b662a59afc2b5120000c6."""


def nb_year(p0: int, percent: float, aug: int, final: int) -> int:
    y: int = 0
    m: int = p0
    percent /= 100

    while m < final:
        m = int(m + (m * percent) + aug)
        y += 1
    return y


def test_growth():
    assert nb_year(1500, 5, 100, 5000) == 15
    assert nb_year(1500000, 2.5, 10000, 2000000) == 10
    assert nb_year(1500000, 0.25, 1000, 2000000) == 94
