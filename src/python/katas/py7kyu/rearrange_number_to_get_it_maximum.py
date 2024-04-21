"""Kata url: https://www.codewars.com/kata/563700da1ac8be8f1e0000dc."""


def max_redigit(num: int) -> int | None:
    if 99 < num < 1000:
        return int("".join(sorted(str(abs(num)), reverse=True)))

    return None


def test_max_redigit():
    assert max_redigit(123) == 321
    assert max_redigit(555) == 555

    assert max_redigit(-1) is None
    assert max_redigit(0) is None
    assert max_redigit(99) is None
    assert max_redigit(1000) is None