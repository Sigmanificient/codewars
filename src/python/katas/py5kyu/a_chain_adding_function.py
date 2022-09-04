"""Kata url: https://www.codewars.com/kata/539a0e4d85e3425cb0000a88."""


class AddableInt(int):

    def __call__(self, other):
        return AddableInt(self + other)


def add(n):
    return AddableInt(n)


def test_add():
    assert add(1) == 1
    assert add(1)(2) == 3
    assert add(1)(2)(3) == 6
