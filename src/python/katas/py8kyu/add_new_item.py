"""Kata url: https://www.codewars.com/kata/596f72bbe7cd7296d1000029."""


def add_extra(lst):
    ret = lst[:]
    ret.append('1')
    return ret


def test_add_extra():
    assert len(add_extra([1, 2])) == 3
    assert len(add_extra([])) == 1
