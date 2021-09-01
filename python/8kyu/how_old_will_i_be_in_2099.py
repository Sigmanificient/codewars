"""Kata url: https://www.codewars.com/kata/5761a717780f8950ce001473."""


def calculate_age(year_of_birth: int, current_year: int) -> str:
    v: int = current_year - year_of_birth

    if not v:
        return 'You were born this very year!'

    if v < 0:
        return f"You will be born in {abs(v)} year{'s' * (abs(v) > 1)}."

    return f"You are {v} year{'s' * (v > 1)} old."
