"""Kata url: https://www.codewars.com/kata/59ffe8bbffe75f6d94000016."""
from typing import Callable, Any, TypeVar

T = TypeVar("T")
AnyFunc = Callable[..., T]


class CallCounter:

    def __init__(self, func: AnyFunc):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs) -> T:
        self.call_count += 1
        return self.func(*args, **kwargs)

    @property
    def __name__(self) -> str:
        return self.func.__name__

    @property
    def __doc__(self) -> str:
        return self.func.__doc__


def count_calls(func: AnyFunc) -> CallCounter:
    return CallCounter(func)


def test_count_calls():
    @count_calls
    def multiply(a, b=1):
        """Calculates the product of a and b."""
        return a * b

    assert multiply.call_count == 0
    assert multiply(2) == 2
    assert multiply.call_count == 1

    assert multiply(3, 6) == 18
    assert multiply.call_count == 2

    assert multiply.__doc__ == "Calculates the product of a and b."
    assert multiply.__name__ == "multiply"

    @count_calls
    def factorial(n):
        return n * factorial(n - 1) if n > 1 else 1

    factorial(10)
    assert factorial.call_count == 10
    factorial(5)
    assert factorial.call_count == 15
