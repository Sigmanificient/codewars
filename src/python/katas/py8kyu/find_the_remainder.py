"""Kata url: https://www.codewars.com/kata/524f5125ad9c12894e00003f."""


def remainder(a, b):
    if b > a:
        a, b = b, a
    return (a % b) if b else None


def test_remainder():
    assert remainder(17, 5) == 2
    assert remainder(13, 72) == remainder(72, 13)
    assert remainder(1, 0) is None
    assert remainder(0, 0) is None
    assert remainder(0, 1) is None
    assert remainder(-1, 0) == 0
    assert remainder(0, -1) == 0
    assert remainder(-13, -13) == 0
    assert remainder(-60, 340) == -20
    assert remainder(60, -40) == -20
