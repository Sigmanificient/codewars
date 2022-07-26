"""Kata url: https://www.codewars.com/kata/57a77726bb9944d000000b06."""


def mango(quantity: int, price: int) -> int:
    return (quantity - quantity // 3) * price


def test_mango():
    assert mango(3, 3) == 6
    assert mango(9, 5) == 30
