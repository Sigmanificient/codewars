"""Kata url: https://www.codewars.com/kata/58a8807c5336a3f613000157."""
square=lambda n,d=1:n if d>=n else n+square(n,d+1)


def test_square():
    for i in range(100):
        assert square(i) == i ** 2
