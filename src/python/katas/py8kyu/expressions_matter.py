"""Kata url: https://www.codewars.com/kata/5ae62fcf252e66d44d00008e."""


def expression_matter(a: int, b: int, c: int) -> int:
    return max((a + b) * c, a + b * c, a * b + c, a * (b + c), a + b + c, a * b * c)


def test_expression_matter():
    assert expression_matter(2, 1, 2) == 6
    assert expression_matter(2, 1, 1) == 4
    assert expression_matter(2, 2, 4) == 16
    assert expression_matter(3, 3, 3) == 27
    assert expression_matter(1, 1, 1) == 3
    assert expression_matter(1, 2, 3) == 9
    assert expression_matter(1, 3, 1) == 5
    assert expression_matter(2, 2, 2) == 8
    assert expression_matter(5, 1, 3) == 20
    assert expression_matter(3, 5, 7) == 105
    assert expression_matter(5, 6, 1) == 35
    assert expression_matter(1, 6, 1) == 8
    assert expression_matter(2, 6, 1) == 14
    assert expression_matter(6, 7, 1) == 48
    assert expression_matter(2, 10, 3) == 60
    assert expression_matter(1, 8, 3) == 27
    assert expression_matter(9, 7, 2) == 126
    assert expression_matter(1, 1, 10) == 20
    assert expression_matter(9, 1, 1) == 18
    assert expression_matter(10, 5, 6) == 300
    assert expression_matter(1, 10, 1) == 12
