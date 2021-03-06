"""Kata url: https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d."""


def halving_sum(n) -> int:
    r: int = n
    while n != 1:
        n //= 2
        r += n

    return r


def test_halving():
    assert halving_sum(25) == 47
    assert halving_sum(127) == 247
