"""Kata url: https://www.codewars.com/kata/570a6a46455d08ff8d001002."""


def no_boring_zeros(n: int) -> int:
    if n == 0:
        return 0

    while not n % 10:
        n //= 10
    return n
