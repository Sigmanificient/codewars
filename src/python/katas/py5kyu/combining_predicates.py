"""Kata url: https://www.codewars.com/kata/626a887e8a33feabd6ad8f25."""


def predicate(func):
    return Predicate(func)


class Predicate:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __or__(self, other):
        return Predicate(
            lambda *args, **kwargs: (
                    self.func(*args, **kwargs)
                    or other.func(*args, **kwargs)
            )
        )

    def __and__(self, other):
        return Predicate(
            lambda *args, **kwargs: (
                    self.func(*args, **kwargs)
                    and other.func(*args, **kwargs)
            )
        )

    def __invert__(self):
        return Predicate(
            lambda *args, **kwargs: not self.func(*args, **kwargs)
        )


def test_predicate():
    @predicate
    def is_even(x):
        return not x % 2

    @predicate
    def is_positive(x):
        return x > 0

    assert (is_even & is_positive)(4)
    assert not (is_even & is_positive)(3)
    assert (is_even | is_positive)(3)
    assert (~is_even & is_positive)(x=3)
