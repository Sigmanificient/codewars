"""Kata url: https://www.codewars.com/kata/563d59dd8e47a5ed220000ba."""


def get_sum_of_digits(n: int) -> int:
    return sum(map(int, str(n)))


def test_get_sum_of_digits():
    assert get_sum_of_digits(0) == 0
    assert get_sum_of_digits(1) == 1
    assert get_sum_of_digits(123) == 6
    assert get_sum_of_digits(223) == 7
