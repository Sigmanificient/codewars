"""Kata url: https://www.codewars.com/kata/59a8570b570190d313000037."""


def sum_cubes(n: int) -> int:
    return sum(x ** 3 for x in range(1, n + 1))
