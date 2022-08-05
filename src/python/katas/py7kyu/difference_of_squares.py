"""Kata url: https://www.codewars.com/kata/558f9f51e85b46e9fa000025."""


def difference_of_squares(n: int) -> int:
    return (sum(range(1, n + 1)) ** 2) - sum(k ** 2 for k in range(1, n + 1))


def test_difference_of_squares():
    assert difference_of_squares(5) == 170
    assert difference_of_squares(10) == 2640
    assert difference_of_squares(100) == 25164150
    assert difference_of_squares(1) == 0
