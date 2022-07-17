"""Kata url: https://www.codewars.com/kata/54fb963d3fe32351f2000102."""


def collatz(n):
    c = 1
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2

        c += 1
    return c


def test_collatz():
    assert collatz(100) == 26
    assert collatz(10) == 7
    assert collatz(500) == 111
    assert collatz(73567465519280238573) == 362
    assert collatz(1000000000) == 101
    assert collatz(1000000000000000) == 276
