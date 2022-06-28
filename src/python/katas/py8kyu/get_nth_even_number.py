"""Kata url: https://www.codewars.com/kata/5933a1f8552bc2750a0000ed."""


def nth_even(n: int) -> int:
    return (n - 1) * 2


def test_nth_even():
    assert nth_even(1) == 0
    assert nth_even(2) == 2
    assert nth_even(3) == 4
    assert nth_even(100) == 198
    assert nth_even(1298734) == 2597466
