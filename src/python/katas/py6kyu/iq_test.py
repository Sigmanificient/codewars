"""Kata url: https://www.codewars.com/kata/552c028c030765286c00007d."""

def iq_test(numbers: str) -> int:
    oddness = [x % 2 for x in map(int, numbers.split())]
    return oddness.index(sum(oddness) == 1) + 1
