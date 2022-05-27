"""Kata url: https://www.codewars.com/kata/5601409514fc93442500010b."""

from typing import List


def better_than_average(class_points: List[int], your_points: int) -> bool:
    return sum(class_points) / len(class_points) < your_points
