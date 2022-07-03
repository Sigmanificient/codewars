"""Kata url: https://www.codewars.com/kata/59fca81a5712f9fa4700159a."""


def to_binary(n: int) -> int:
    return int(f'{n:b}')


def test_to_binary():
    assert to_binary(1) == 1
    assert to_binary(2) == 10
    assert to_binary(3) == 11
    assert to_binary(5) == 101
