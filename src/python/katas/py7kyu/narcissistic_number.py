"""Kata url: https://www.codewars.com/kata/56b22765e1007b79f2000079."""


def is_narcissistic(i: int) -> int:
    return sum(int(k) ** len(str(i)) for k in str(i)) == i


def test_is_narcissistic():
    assert is_narcissistic(153)
    assert is_narcissistic(371)
    assert is_narcissistic(407)
    assert is_narcissistic(1634)

    assert not is_narcissistic(595)
    assert not is_narcissistic(825)
    assert not is_narcissistic(201)
    assert not is_narcissistic(259)
