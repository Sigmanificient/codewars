"""Kata url: https://www.codewars.com/kata/6071ef9cbe6ec400228d9531."""
import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '//': operator.ifloordiv
}


def calculator(txt):
    x, op, y = txt.split(' ')
    return OPERATIONS.get(op)(len(x), len(y)) * '.'
