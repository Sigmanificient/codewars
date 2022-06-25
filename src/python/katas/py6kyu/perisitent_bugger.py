"""Kata url: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec."""


def mul(*args: int) -> int:
    x = 1
    for k in args:
        x *= k
    return x


def persistence(n: int) -> int:
    i = 0
    while n > 9:
        n = mul(*map(int, str(n)))
        i += 1

    return i


def test_mul():
    assert mul(0) == 0
    assert mul(1) == 1

    assert mul(1, 2, 3) == 6
    assert mul(1, 2, 3, 4) == 24
    assert mul(1, 2, 3, 4, 5) == 120

    assert mul(1, 2, 3, 4, 5, 6, 0) == 0
    assert mul(1, 1, 1, 1, 1, 1, 1, 1) == 1
    assert mul(1, 1, 1, 1, 1, 1, 1, -1) == -1


def test_persistence():
    assert persistence(0) == 0
    assert persistence(4) == 0
    assert persistence(25) == 2
    assert persistence(39) == 3
    assert persistence(999) == 4
    assert persistence(3301) == 1
