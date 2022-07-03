"""Kata url: https://www.codewars.com/kata/577a6e90d48e51c55e000217."""


def hotpo(n: int) -> int:
    c: int = 0
    while n != 1:
        n = (3 * n + 1) if n % 2 else n // 2
        c += 1

    return c


def test_hotpo():
    assert hotpo(1) == 0
    assert hotpo(5) == 5
    assert hotpo(6) == 8
    assert hotpo(23) == 15
