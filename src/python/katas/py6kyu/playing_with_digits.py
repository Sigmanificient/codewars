"""Kata url: https://www.codewars.com/kata/5552101f47fc5178b1000050."""


def dig_pow(n: int, p: int) -> int:
    r: int = 0
    for digit in str(n):
        r += int(digit) ** p
        p += 1

    return r // n if (r % n) == 0 else -1


def test_dig_pow():
    assert dig_pow(89, 1) == 1
    assert dig_pow(92, 1) == -1
    assert dig_pow(46288, 3) == 51
