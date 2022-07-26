"""Kata url: https://www.codewars.com/kata/58dced7b702b805b200000be."""
from dataclasses import dataclass
from math import sqrt


@dataclass
class Point:
    x: int
    y: int


def distance_between_points(a: Point, b: Point) -> float:
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def test_distance_between_points():
    assert distance_between_points(Point(3, 3), Point(3, 3)) == 0
    assert distance_between_points(Point(1, 6), Point(4, 2)) == 5
    assert (
        round(distance_between_points(Point(-10.2, 12.5), Point(0.3, 14.7)), 6)
        == 10.728001
    )
    assert round(distance_between_points(Point(0, 0), Point(0, 0)), 6) == 0
