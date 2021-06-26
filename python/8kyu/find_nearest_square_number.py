from math import sqrt


def nearest_sq(n: int) -> int:
    """Kata url: https://www.codewars.com/kata/5a805d8cafa10f8b930005ba."""
    return round(sqrt(n)) ** 2
