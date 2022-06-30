"""Kata url: https://www.codewars.com/kata/57f36495c0bb25ecf50000e7."""


def find(n: int) -> int:
    return sum(k for k in range(n + 1) if not (k % 3 and k % 5))


def test_find():
    assert find(1) == 0
    assert find(3) == 3
    assert find(5) == 8
    assert find(10) == 33
    assert find(1000) == 234168
