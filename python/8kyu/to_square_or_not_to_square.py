from math import sqrt


def square_or_square_root(arr):
    """Kata url: https://www.codewars.com/kata/57f6ad55cca6e045d2000627."""
    return [x ** 2 if (s := sqrt(x)) % 1 else s for x in arr]
