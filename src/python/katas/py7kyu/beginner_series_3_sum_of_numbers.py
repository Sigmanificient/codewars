"""Kata url: https://www.codewars.com/kata/55f2b110f61eb01779000053."""


def get_sum(a: int, b: int) -> int:
    if b < a:
        a, b = b, a

    return sum(range(a, b + 1))


def test_get_sum():
    assert get_sum(0, 1), 1
    assert get_sum(0, -1) == -1
