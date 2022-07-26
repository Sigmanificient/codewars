"""Kata url: https://www.codewars.com/kata/5bc5c064eba26ef6ed000158."""


def silent_thief(module_name: str) -> str:
    x = lambda o, n: getattr(o, n.center(len(n) + 4, "_"))
    return x(x(breakpoint, "self"), "imp" + "ort")(module_name)


def test_silent_thief():
    math = silent_thief("math")
    import math as also_math

    assert math == also_math
