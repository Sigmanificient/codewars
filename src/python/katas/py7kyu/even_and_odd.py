"""Kata url: https://www.codewars.com/kata/594adadee075005308000122."""

from typing import Tuple


def even_and_odd(n) -> Tuple[int, int]:
    ne = no = ""

    for x in str(n):
        if int(x) % 2:
            ne += x
        else:
            no += x

    return int(no or "0"), int(ne or "0")


def test_even_and_odd():
    assert even_and_odd(126453) == (264, 153)
    assert even_and_odd(3012) == (2, 31)
    assert even_and_odd(4628) == (4628, 0)
