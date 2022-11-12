"""Kata url: https://www.codewars.com/kata/538835ae443aae6e03000547."""


def add(n):
    return lambda i: n + i


def test_add():
    assert add(1)(3) == 4
    assert add(0)(-15) == -15

    add_three = add(3)
    assert add_three(5) == 8
    assert add_three(5) == 8
