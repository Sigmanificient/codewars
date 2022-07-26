"""Kata url: https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f."""


def compute_sum(n: int) -> int:
    return sum(map(lambda k: sum(map(int, str(k))), range(1, n + 1)))


def test_compute_sum():
    assert compute_sum(1) == 1
    assert compute_sum(2) == 3
    assert compute_sum(3) == 6
    assert compute_sum(4) == 10
    assert compute_sum(10) == 46
    assert compute_sum(100) == 901
