"""Kata url: https://www.codewars.com/kata/52f78966747862fc9a0009ae."""
import operator
import re

FLOAT_REGEX = re.compile(r'^\d+\.\d+$')
OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def calc(expr: str):
    if not expr:
        return 0

    stack = []
    factors = expr.split()

    for f in factors:
        if f in OPS:
            x, y = stack.pop(), stack.pop()
            stack.append(OPS[f](y, x))
            continue

        stack.append(float(f) if FLOAT_REGEX.match(f) else int(f))
    return stack.pop() if stack else 0


def test_calc():
    assert calc("") == 0
    assert calc("3") == 3
    assert calc("3.5") == 3.5
    assert calc("1 3 +") == 4
    assert calc("1 3 *") == 3
    assert calc("1 3 -") == -2
    assert calc("4 2 /") == 2
