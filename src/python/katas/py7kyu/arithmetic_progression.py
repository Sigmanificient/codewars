"""Kata url: https://www.codewars.com/kata/55caf1fd8063ddfa8e000018."""


def arithmetic_sequence_elements(a: int, d: int, n: int) -> str:
    return ', '.join(map(str, (a + (d * i) for i in range(n))))


def test_arithmetic_sequence_elements():
    f = arithmetic_sequence_elements
    assert f(1, 2, 5) == '1, 3, 5, 7, 9'
    assert f(1, 0, 5) == '1, 1, 1, 1, 1'
    assert f(1, -3, 10) == '1, -2, -5, -8, -11, -14, -17, -20, -23, -26'
