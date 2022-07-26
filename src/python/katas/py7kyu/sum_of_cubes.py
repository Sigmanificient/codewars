"""Kata url: https://www.codewars.com/kata/59a8570b570190d313000037."""


def sum_cubes(n: int) -> int:
    return sum(x**3 for x in range(1, n + 1))


def test_sum_cubes():
    assert sum_cubes(1) == 1
    assert sum_cubes(2) == 9
    assert sum_cubes(3) == 36
    assert sum_cubes(4) == 100
    assert sum_cubes(10) == 3025
    assert sum_cubes(123) == 58155876
    assert sum_cubes(0) == 0
