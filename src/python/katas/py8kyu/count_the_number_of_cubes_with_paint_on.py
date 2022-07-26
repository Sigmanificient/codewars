"""Kata url: https://www.codewars.com/kata/5763bb0af716cad8fb000580."""


def count_squares(cuts: int) -> int:
    cuts += 1
    return (cuts**3) - ((cuts - 2) ** 3)


def test_count_squares():
    assert count_squares(5) == 152
    assert count_squares(16) == 1538
    assert count_squares(23) == 3176
