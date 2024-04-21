"""Kata url: https://www.codewars.com/kata/60cf559c068ae600468f8e5a."""


def reverse_float_decimal(n: float) -> float:
    return int(n) + float(f"0.{str(round(n % 1, 5))[2:][::-1]}")


def test_reverse_float_decimal():
    def float_eq(left, right, thresold = 0.000001) -> bool:
        return abs(left - right) < thresold


    assert float_eq(reverse_float_decimal(2.5), 2.5)
    assert float_eq(reverse_float_decimal(1.12345), 1.54321)
    assert float_eq(reverse_float_decimal(7.0007), 7.7)