"""Kata url: https://www.codewars.com/kata/5641a03210e973055a00000d."""


def two_decimal_places(n: float) -> float:
    return round(n, 2)


def test_two_decimal_places():
    assert (two_decimal_places(4.659725356) - 4.66) < 0.001
    assert (
        two_decimal_places(173735326.3783732637948948) - 173735326.38
    ) < 0.01
    assert (two_decimal_places(4.653725356) - 4.65) < 0.001