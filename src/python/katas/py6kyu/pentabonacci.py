"""Kata url: https://www.codewars.com/kata/55c9172ee4bb15af9000005d."""


def count_odd_pentafib(n: int) -> int:
    if not n:
        return 0

    i = k = 0
    pent = [0, 1, 1, 2, 4]
    c = 1

    if n < 5:
        return c

    for _ in range(n - 4):
        k = sum(pent)
        if k % 2:
            c += 1

        pent[i] = k
        i = (i + 1) % 5

    return c


def test_count_odd_pentafib():
    assert count_odd_pentafib(5) == 1
    assert count_odd_pentafib(10) == 3
    assert count_odd_pentafib(15) == 5
    assert count_odd_pentafib(45) == 15
    assert count_odd_pentafib(68) == 23
    assert count_odd_pentafib(0) == 0
    assert count_odd_pentafib(1) == 1
    assert count_odd_pentafib(2) == 1
