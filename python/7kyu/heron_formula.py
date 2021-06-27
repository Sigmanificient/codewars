from math import sqrt


def heron(a: int, b: int, c: int) -> float:
    """Kata url: https://www.codewars.com/kata/57aa218e72292d98d500240f."""
    s = (a + b + c) / 2
    return round(sqrt(s * (s - a) * (s - b) * (s - c)), 2)
