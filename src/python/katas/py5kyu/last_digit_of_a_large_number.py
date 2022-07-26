"""Kata url: https://www.codewars.com/kata/5511b2f550906349a70004e1."""


def last_digit(a: int, b: int) -> int:
    return pow(a, b, 10)


def test_last_digit():
    assert last_digit(4, 1) == 4
    assert last_digit(4, 2) == 6
    assert last_digit(9, 7) == 9
    assert last_digit(10, 10**10) == 0
    assert last_digit(2**200, 2**300) == 6
    assert (
        last_digit(
            3715290469715693021198967285016729344580685479654510946723,
            68819615221552997273737174557165657483427362207517952651,
        )
        == 7
    )

    for n in range(1, 9):
        assert last_digit(n**n, 0) == 1
