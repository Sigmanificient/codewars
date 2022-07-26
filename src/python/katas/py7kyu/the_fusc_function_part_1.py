"""Kata url: https://www.codewars.com/kata/570409d3d80ec699af001bf9."""


def fusc(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n % 2:
        n //= 2
        return fusc(n) + fusc(n + 1)

    return fusc(n // 2)


def test_fusc():
    assert fusc(0) == 0
    assert fusc(1) == 1
    assert [fusc(i) for i in range(21)] == [
        0,
        1,
        1,
        2,
        1,
        3,
        2,
        3,
        1,
        4,
        3,
        5,
        2,
        5,
        3,
        4,
        1,
        5,
        4,
        7,
        3,
    ]
    assert fusc(85) == 21
