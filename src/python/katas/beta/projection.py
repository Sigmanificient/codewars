"""Kata url: https://www.codewars.com/kata/62dfc7edc1e633b815fae046."""
from typing import List


def project(light_source: List[int], point: List[int], screen_x: int) -> List[int]:
    a, b, c = point
    d, e, f = light_source

    u = (screen_x - a) / (d - a)

    return [screen_x, int(b + (e - b) * u), int(c + (f - c) * u)]


def test_project():
    assert project([0, 87, -66], [616, -139, 12], 899) == [899, -242, 47]
    assert project([0, -52, 16], [223, 62, -111], 346) == [346, 124, -181]
    assert project([0, -48, 67], [209, -84, -47], 210) == [210, -84, -47]
    assert project([0, 18, -9], [448, -31, -43], 536) == [536, -40, -49]
    assert project([0, -90, 17], [367, -52, -120], 573) == [573, -30, -196]
