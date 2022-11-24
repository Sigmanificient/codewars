"""Kata url: https://www.codewars.com/kata/52988f3f7edba9839c00037d."""


def reject(seq, predicate):
    return [x for x in seq if not predicate(x)]


def test_reject():
    assert reject([1, 2, 3, 4, 5, 6], lambda x: x%2==0) == [1, 3, 5]
    assert reject(['a', 'b', 3, 'd'], lambda x: type(x)==int) == ['a', 'b', 'd']
    assert reject(['a', 'b', 3, 'd'], lambda x: type(x)==str) == [3]
