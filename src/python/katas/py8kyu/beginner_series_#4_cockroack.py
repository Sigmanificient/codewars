"""Kata url: https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6."""

from typing import Union


def cockroach_speed(s: Union[int, float]) -> int:
    return int((s * 1000) // 36)
