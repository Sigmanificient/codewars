"""Kata url: https://www.codewars.com/kata/55685cd7ad70877c23000102."""


def make_negative(number: int) -> int:
    return -abs(number)

def test_negative():
    for n, expected in ((42, -42), (-9, -9), (0, 0)):
        assert  make_negative(n) == expected