"""Kata url: https://www.codewars.com/kata/5541f58a944b85ce6d00006a."""
from typing import List


def product_fib(prod: int) -> List[int]:
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b

    return [a, b, a * b == prod]


def test_product_fib():
    assert product_fib(4895) == [55, 89, True]
    assert product_fib(5895) == [89, 144, False]

    assert product_fib(74049690) == [6765, 10946, True]
    assert product_fib(84049690) == [10946, 17711, False]


