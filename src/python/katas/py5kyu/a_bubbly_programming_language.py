"""Kata url: https://www.codewars.com/kata/5f7a715f6c1f810017c3eb07."""

import operator

_handle = lambda n, do, *a: (do(*a), end.pop() if n == end else n)[1]
_calc = lambda op: stack.append(op(stack.pop(), stack.pop()))
_mk_op = lambda op: lambda n: _handle(n, _calc, op)

start = lambda n: _handle(n, stack.clear)
stack = end = []
push = lambda item: lambda n: _handle(n, stack.append, item)
add = _mk_op(operator.add)
sub = _mk_op(operator.sub)
mul = _mk_op(operator.mul)
div = _mk_op(operator.floordiv)