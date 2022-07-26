"""Kata url: https://www.codewars.com/kata/57a429e253ba3381850000fb."""


def bmi(weight: float, height: float) -> str:
    bmi: float = weight / height**2

    if bmi <= 18.5:
        return "Underweight"

    if bmi <= 25.0:
        return "Normal"

    if bmi <= 30.0:
        return "Overweight"

    return "Obese"


def test_bmi():
    assert bmi(50, 1.80) == "Underweight"
    assert bmi(80, 1.80) == "Normal"
    assert bmi(90, 1.80) == "Overweight"
    assert bmi(110, 1.80) == "Obese"
    assert bmi(50, 1.50) == "Normal"
