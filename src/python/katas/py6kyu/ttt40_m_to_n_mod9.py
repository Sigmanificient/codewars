"""Kata url: https://www.codewars.com/kata/57b2cef5d2a31c3965000a43."""

def n_mod9(m: int, n: int) -> int:
    n %= 9
    m %= 9

    m = -(9 - m) if m > n else m
    return sum(range(m, n + 1)) % 9