"""Kata url: https://www.codewars.com/kata/57356c55867b9b7a60000bd7."""

from typing import Dict, Union, Callable

ops: Dict[str, Callable[[int, int], Union[int, float]]] = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def basic_op(operator, value1, value2) -> Union[int, float]:
    return ops[operator](value1, value2)


def test_basic_op():
    assert basic_op("+", 4, 7) == 11
    assert basic_op("-", 15, 18) == -3
    assert basic_op("*", 5, 5) == 25
    assert basic_op("/", 49, 7) == 7

    assert basic_op("+", 1, 5) == 6
    assert basic_op("-", 5, 1) == 4
    assert basic_op("*", 2, 2) == 4
    assert basic_op("/", 4, 2) == 2
