"""Kata url: https://www.codewars.com/kata/5c5086287bc6600001c7589a."""


def is_negative_zero(n: float) -> bool:
    return str(n) == '-0.0'


def test_is_negative_zero():
    assert is_negative_zero(-0.0)
    assert not is_negative_zero(-(float("inf")))
    assert not is_negative_zero(-5.0)
    assert not is_negative_zero(-4.0)
    assert not is_negative_zero(-3.0)
    assert not is_negative_zero(-2.0)
    assert not is_negative_zero(-1.0)
    assert not is_negative_zero(0.0)
    assert not is_negative_zero(1.0)
    assert not is_negative_zero(2.0)
    assert not is_negative_zero(3.0)
    assert not is_negative_zero(4.0)
    assert not is_negative_zero(5.0)
    assert not is_negative_zero(float("inf"))
