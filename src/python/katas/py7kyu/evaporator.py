"""Kata url: https://www.codewars.com/kata/5506b230a11c0aeab3000c1f."""


def evaporator(content: float, evap_per_day: int, threshold: int) -> int:
    c: int = 0
    mn: float = content * (threshold / 100)

    while content > mn:
        content *= 1 - (evap_per_day / 100)
        c += 1
    return c
