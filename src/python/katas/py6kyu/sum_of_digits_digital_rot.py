"""Kata url: https://www.codewars.com/kata/541c8630095125aba6000c00."""


def digital_root(n: int) -> int:
    while n > 9:
        n = sum(map(int, str(n)))

    return n


def test_digital_root():
    assert digital_root(16) == 7
    assert digital_root(942) == 6
    assert digital_root(132189) == 6
    assert digital_root(493193) == 2
