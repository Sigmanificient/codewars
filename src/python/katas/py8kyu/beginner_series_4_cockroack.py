"""Kata url: https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6."""

from typing import Union


def cockroach_speed(s: Union[int, float]) -> int:
    return int((s * 1000) // 36)


def test_cockroach_speed():
    assert cockroach_speed(0) == 0
    assert cockroach_speed(1.08) == 30
    assert cockroach_speed(1.09) == 30
    assert cockroach_speed(2) == 55
    assert cockroach_speed(3) == 83
