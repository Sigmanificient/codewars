"""Kata url: https://www.codewars.com/kata/54d1c59aba326343c80000e7."""


def divide_numbers(x: int, y: int) -> float:
    return x / y


def _float_eq(
    left: float | int,
    right: float | int,
    threshold = 0.001
) -> bool:
    return abs(left - right) < threshold

def test_divide_numbers():
    assert divide_numbers(4, 2) == 2
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(9, 3) == 3
    assert _float_eq(divide_numbers(9, 4), 2.25)
    assert _float_eq(divide_numbers(21, 5), 4.2)
    assert _float_eq(divide_numbers(1, 100), 0.01)