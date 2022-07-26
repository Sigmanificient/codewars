"""Kata url: https://www.codewars.com/kata/56606694ec01347ce800001b."""


def is_triangle(a: int, b: int, c: int) -> bool:
    m = max((a, b, c))
    return (a + b + c) - m > m


def test_is_triangle():
    assert is_triangle(1, 2, 2)
    assert is_triangle(4, 2, 3)
    assert is_triangle(5, 1, 5)
    assert is_triangle(2, 2, 2)

    assert not is_triangle(7, 2, 2)
    assert not is_triangle(1, 2, 3)
    assert not is_triangle(1, 3, 2)
    assert not is_triangle(3, 1, 2)
    assert not is_triangle(5, 1, 2)
    assert not is_triangle(1, 2, 5)
    assert not is_triangle(2, 5, 1)
    assert not is_triangle(-1, 2, 3)
    assert not is_triangle(1, -2, 3)
    assert not is_triangle(1, 2, -3)
    assert not is_triangle(0, 2, 3)
