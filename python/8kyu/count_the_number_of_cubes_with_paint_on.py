"""Kata url: https://www.codewars.com/kata/5763bb0af716cad8fb000580."""


def count_squares(cuts: int) -> int:
    cuts += 1
    return (cuts ** 3) - ((cuts - 2) ** 3)
