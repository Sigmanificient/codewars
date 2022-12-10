"""Kata url: https://www.codewars.com/kata/5421c6a2dda52688f6000af8."""


def compose(f, g):
    def wrapper(*h):
        return f(g(*h))
    return wrapper


def test_compose():
    funcs = [
        lambda x: x + 1,
        lambda x: x - 1,
        lambda x: x / 2,
        lambda x: x + 15,
        lambda x: x,
        lambda *args: sum(args),
    ]

    assert compose(funcs[0], funcs[4])(0) == 1
    assert compose(funcs[0], funcs[2])(2) == 2
    assert compose(funcs[0], funcs[5])(1, 2, 3, 4, 5) == 16

    assert compose(funcs[3], funcs[4])(0) == 15
    assert compose(funcs[4], funcs[3])(0) == 15
