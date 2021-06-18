from typing import Dict, Union, Callable

ops: Dict[str, Callable[[int, int], Union[int, float]]] = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}


def basic_op(operator, value1, value2) -> Union[int, float]:
    """Kate url: https://www.codewars.com/kata/57356c55867b9b7a60000bd7."""
    return ops[operator](value1, value2)
