"""Kata url: https://www.codewars.com/kata/569e09850a8e371ab200000b."""


from typing import List


def pre_fizz(n: int) -> List[int]:
    return list(range(1, n + 1))


def test_pre_fizz():
    assert pre_fizz(1) == [1]
    assert pre_fizz(2) == [1, 2]
    assert pre_fizz(3) == [1, 2, 3]
    assert pre_fizz(4) == [1, 2, 3, 4]
    assert pre_fizz(5) == [1, 2, 3, 4, 5]
