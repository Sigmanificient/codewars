"""Kata url: https://www.codewars.com/kata/54d1c59aba326343c80000e7."""


def divide_numbers(x: int, y: int) -> float:
    return x / y


def test_divide_numbers():
    assert divide_numbers(4, 2) == 2
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(9, 4) == 2.25
    assert divide_numbers(21, 5) == 4.2
    assert divide_numbers(9, 3) == 3
    assert divide_numbers(1, 100) == 0.01
