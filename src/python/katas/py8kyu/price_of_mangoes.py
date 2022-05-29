"""Kata url: https://www.codewars.com/kata/57a77726bb9944d000000b06."""


def mango(quantity: int, price: int) -> int:
    return (quantity - quantity//3) * price
