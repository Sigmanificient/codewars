from typing import Dict, Union, Callable

ops: Dict[str: Callable[[int, int], Union[int, float]]] = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}


def basic_op(operator, value1, value2) -> Union[int, float]:
    return ops[operator](value1, value2)
