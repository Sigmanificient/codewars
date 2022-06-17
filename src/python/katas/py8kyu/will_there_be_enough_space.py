"""Kata url: https://www.codewars.com/kata/5875b200d520904a04000003."""


def enough(cap: int, on: int, wait: int) -> int:
    is_enough: bool = (cap - on) > wait
    return 0 if is_enough else abs((cap - on) - wait)


def test_enough():
    assert enough(10, 5, 5) == 0
    assert enough(100, 60, 50) == 10
    assert enough(20, 5, 5) == 0
