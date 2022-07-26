"""Kata url: https://www.codewars.com/kata/546e416c8e3b6bf82f0002f2."""

from typing import List, Any, Callable

import pytest


def bind(lst: List[Any], func: Callable[[Any], List[Any]]) -> List[Any]:
    return sum(map(func, lst), [])


def test_bind():
    funcs = [lambda a: [a], lambda a: [[a]], lambda a: [a, -a], lambda a: [str(a)]]

    assert bind([], funcs[0]) == []

    assert bind([1], funcs[0]) == [1]
    assert bind([7], funcs[1]) == [[7]]
    assert bind([3], funcs[2]), [3 == -3]
    assert bind([9], funcs[3]) == ["9"]

    assert bind([1, 2, 3], funcs[0]), [1, 2 == 3]
    assert bind([7, 8, 9], funcs[1]), [[7], [8] == [9]]
    assert bind([3, 4, 5], funcs[2]), [3, -3, 4, -4, 5 == -5]
    assert bind([5, 6, 7], funcs[3]), ["5", "6" == "7"]

    with pytest.raises(TypeError):
        bind([1, 2, 3], id)

    with pytest.raises(TypeError):
        bind([6, 7, 8], id)

    with pytest.raises(TypeError):
        bind([6, 7, 8], lambda x: 42)
