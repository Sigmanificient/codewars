"""Kata url: https://www.codewars.com/kata/5aff237c578a14752d0035ae."""
import math


def predict_age(*ages: int) -> int:
    return math.sqrt(sum(age * age for age in ages)) // 2
