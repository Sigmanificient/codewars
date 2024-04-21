"""Kata url: https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4."""

from __future__ import annotations

from math import sqrt
from typing import List, Callable

import pytest

Op = Callable[[int, int], int]


class Vector:
    def __init__(self, values: List[int]):
        self.__values = values

    def __iter__(self):
        return iter(self.__values)

    def __len__(self):
        return len(self.__values)

    def __str__(self):
        return f"({','.join(map(str, self))})"

    def __inner_map(self, other: Vector, op: Op) -> Vector:
        if len(self) != len(other):
            raise ValueError("Values are different length")

        return Vector([op(x, y) for x, y in zip(self, other)])

    def add(self, other: Vector) -> Vector:
        return self.__inner_map(other, int.__add__)

    def subtract(self, other: Vector) -> Vector:
        return self.__inner_map(other, int.__sub__)

    def dot(self, other: Vector) -> int:
        return sum(x * y for x, y in zip(self, other))

    def norm(self) -> float:
        return sqrt(sum(x**2 for x in self))

    def equals(self, other: Vector):
        return all(x == y for x, y in zip(self, other))


def test_vector():
    import math

    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])
    c = Vector([5, 6, 7, 8])

    assert a.add(b).equals(Vector([4, 6, 8]))
    assert a.subtract(b).equals(Vector([-2, -2, -2]))

    assert a.dot(b) == 26
    assert b.dot(a) == a.dot(b)

    assert a.norm() - math.sqrt(14) < 0.1
    assert b.norm() - math.sqrt(50) < 0.1
    assert c.norm() - math.sqrt(174) < 0.1

    assert a.equals(Vector([1, 2, 3]))
    assert b.equals(Vector([3, 4, 5]))
    assert not a.equals(b)
    assert not b.equals(c)
    assert not a.equals(c)

    assert str(a) == "(1,2,3)"
    assert str(b) == "(3,4,5)"
    assert str(c) == "(5,6,7,8)"

    with pytest.raises(ValueError):
        a.add(c)