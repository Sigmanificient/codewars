"""Kata url: https://www.codewars.com/kata/51e04f6b544cf3f6550000c1."""

def beeramid(bonus: int, price: int) -> int:
    total = 0
    n = 1

    while True:
        total += price * (n ** 2)
        if total > bonus:
            return n - 1

        n += 1