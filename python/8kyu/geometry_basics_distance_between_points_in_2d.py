from math import sqrt


class Point:
    __slots__ = ('x', 'y')


def distance_between_points(a: Point, b: Point) -> float:
    """Kata url: https://www.codewars.com/kata/58dced7b702b805b200000be."""
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
