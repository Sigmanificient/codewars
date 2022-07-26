"""Kata url: https://www.codewars.com/kata/57241e0f440cd279b5000829."""


def sum_mul(n: int, m: int) -> int:
    if n <= 0 or m <= 0:
        return "INVALID"

    return 0 if m < n else sum(range(n, m, n))


def test_sum_mul():
    assert sum_mul(4, 123) == 1860
    assert sum_mul(123, 4567) == 86469
    assert sum_mul(2, 10) == 20
    assert sum_mul(2, 2) == 0
    assert sum_mul(7, 7) == 0
    assert sum_mul(7, 2) == 0
    assert sum_mul(21, 3) == 0
    assert sum_mul(0, 2) == "INVALID"
    assert sum_mul(2, 0) == "INVALID"
    assert sum_mul(4, -7) == "INVALID"
    assert sum_mul(-7, 4) == "INVALID"
