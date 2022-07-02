# Kata url: https://www.codewars.com/kata/5926d7494b2b1843780001e6.


def add(*n: int) -> int:
    return sum(n)


def test_add():
    assert add() == 0
    assert add(2) == 2
    assert add(1, 1) == 2
    assert add(1, 2, 3) == 6
    assert add(-3, -2, -1, 1, 2, 3, 4) == 4
