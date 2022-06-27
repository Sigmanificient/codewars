"""Kata url: https://www.codewars.com/kata/555a67db74814aa4ee0001b5."""


def is_even(n: int) -> int:
    return not n % 2


def test_is_event():
    assert is_even(0)
    assert not is_even(0.5)
    assert not is_even(1)
    assert is_even(2)
    assert is_even(-4)
    assert not is_even(15)
    assert is_even(20)
    assert is_even(220)
    assert not is_even(222222221)
    assert is_even(500000000)
