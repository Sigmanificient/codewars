"""Kata url: https://www.codewars.com/kata/5810085c533d69f4980001cf."""

from typing import Union, Callable, Dict


opts: Dict[str, Callable[[int, int], Union[int, float]]] = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}


def calculator(
    x: Union[int, str], y: Union[int, str], op: str
) -> Union[int, str]:
    op = opts.get(op)
    return op(x, y) if callable(op) and isinstance(x, int) and isinstance(y, int) else "unknown value"
