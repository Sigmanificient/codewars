"""Kata url: https://www.codewars.com/kata/583f158ea20cfcbeb400000a."""

ops = {
    'add': int.__add__,
    'subtract': int.__sub__,
    'multiply': int.__mul__,
    'divide': int.__truediv__
}


def arithmetic(a: int, b: int, operator) -> int:
    return ops[operator](a, b)


def test_arithmetic():
    assert arithmetic(1, 2, "add") == 3
    assert arithmetic(8, 2, "subtract") == 6
    assert arithmetic(5, 2, "multiply") == 10
    assert arithmetic(8, 2, "divide") == 4
