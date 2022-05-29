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
) -> Union[float, str]:
    _err: str = "unknown value"

    if not isinstance(x, int) or not isinstance(y, int):
        return _err

    func = opts.get(op)
    if func is None:
        return _err

    return func(x, y)
