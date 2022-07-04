"""Kata url: https://www.codewars.com/kata/546e2562b03326a88e000020. """


def square_digits(num: int) -> int:
    return int(''.join(str(int(digit) ** 2) for digit in str(num)))


def test_square_digits():
    assert square_digits(0) == 0
    assert square_digits(2) == 4
    assert square_digits(9119) == 811181
