"""Kata url: https://www.codewars.com/kata/587c2d08bb65b5e8040004fd."""


def nba_extrap(ppg: int, mpg: int) -> float:
    return round((ppg / mpg) * 48, 1) or 0
