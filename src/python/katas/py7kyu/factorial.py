"""Kata url: https://www.codewars.com/kata/57a049e253ba33ac5e000212."""


def factorial(n: int) -> int:
    return n * factorial(n - 1) if n else 1


def test_factorial():
    tests = (
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
    )

    for inp, exp in tests:
        assert factorial(inp) == exp
