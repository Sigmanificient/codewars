"""Kata url: https://www.codewars.com/kata/577e9095d648a15b800000d4."""

import math
from typing import Union, Callable, List, Dict


Operand = Callable[[int, int], int]
OPS_FUNCS: Dict[str, Operand] = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

Token = Union[int, Operand]


def postfix_evaluator(expr: str) -> int:
    ints: List[int] = []

    for fac in expr.split(' '):
        tok: Token = int(fac) if fac[-1].isdigit() else OPS_FUNCS[fac]

        if isinstance(tok, int):
            ints.append(tok)
            continue

        op: Operand = tok
        right = ints.pop()
        left = ints.pop()

        r = math.floor(op(left, right))
        ints.append(r)

    return ints.pop()


def test_postfix_evaluator():
    assert postfix_evaluator("2 3 +") == 5
    assert postfix_evaluator("2 -3 +") == -1
    assert postfix_evaluator("1") == 1
    assert postfix_evaluator("-1") == -1
    assert postfix_evaluator("2 3 9 4 / + *") == 10
    assert postfix_evaluator("3 4 9 / *") == 0
    assert postfix_evaluator("4 8 + 6 5 - * 3 2 - 2 2 + * /") == 3
    assert postfix_evaluator("2 3 9 4 / + *") == 10
    assert postfix_evaluator("3 4 9 / *") == 0
    assert postfix_evaluator("4 8 + 6 5 - * 3 2 - 2 2 + * /") == 3
    assert postfix_evaluator("21 21 +") == 42
    assert postfix_evaluator("-42 42 +") == 0
