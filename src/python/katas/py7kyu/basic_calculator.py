"""Kata url: https://www.codewars.com/kata/5296455e4fe0cdf2e000059f."""


def calculate(a, op, b):
    return {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y else None
    }.get(op, lambda *_: None)(a, b)


def test_calculate():
    assert calculate(3.2, "+", 8) == 11.2
    assert calculate(3.2, "-", 8) == -4.8
    assert calculate(3.2, "/", 8) == 0.4
    assert calculate(3.2, "*", 8) == 25.6
    assert calculate(-3, "+", 0) == -3
    assert calculate(-3, "-", 0) == -3
    assert calculate(-2, "/", -2) == 1
    assert calculate(-3, "*", 0) == 0

    assert calculate(-3, "/", 0) is None
    assert calculate(-3, "w", 0) is None
    assert calculate(-3, "w", 1) is None
