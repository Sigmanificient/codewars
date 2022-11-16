"""Kata url: https://www.codewars.com/kata/58c9322bedb4235468000019."""


def is_very_even_number(n):
    if n < 10:
        return not n & 1

    return is_very_even_number(sum(map(int, str(n))))


def test_is_very_even_number():
    assert is_very_even_number(0)
    assert is_very_even_number(4)
    assert not is_very_even_number(12)
    assert is_very_even_number(222)
    assert not is_very_even_number(5)
    assert not is_very_even_number(45)
    assert not is_very_even_number(4554)
    assert not is_very_even_number(1234)
    assert not is_very_even_number(88)
    assert is_very_even_number(24)
    assert is_very_even_number(40000022)
