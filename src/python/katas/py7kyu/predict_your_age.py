"""Kata url: https://www.codewars.com/kata/5aff237c578a14752d0035ae."""
import math


def predict_age(*ages: int) -> int:
    return math.sqrt(sum(age * age for age in ages)) // 2


def test_predict_age():
    assert predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
    assert predict_age(45, 55, 29, 34, 43, 65, 45, 62) == 68
    assert predict_age(45, 55, 29, 34, 43, 65, 45, 62, 45) == 72
