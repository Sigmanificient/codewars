"""Kata url: https://www.codewars.com/kata/58dced7b702b805b200000be."""

from math import sqrt
from typing import Tuple


class Point:
    __slots__: Tuple[str] = ('x', 'y')


def distance_between_points(a: Point, b: Point) -> float:
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
