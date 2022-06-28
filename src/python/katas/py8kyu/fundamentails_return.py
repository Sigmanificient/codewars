"""Kata url: https://www.codewars.com/kata/55a5befdf16499bffb00007b."""


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    return a / b


def mod(a: int, b: int) -> int:
    return a % b


def exponent(a: int, b: int) -> int:
    return a ** b


def subt(a: int, b: int) -> int:
    return a - b


def test_add():
    assert add(1, 2) == 3
    assert add(1, -2) == -1
    assert add(3, 3) == 6
    assert add(3, -3) == 0


def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(1, -2) == -2
    assert multiply(3, 3) == 9
    assert multiply(3, -3) == -9


def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(1, -2) == -0.5
    assert divide(3, 3) == 1
    assert divide(3, -3) == -1


def test_mod():
    assert mod(1, 2) == 1
    assert mod(1, -2) == -1
    assert mod(3, 3) == 0
    assert mod(3, -3) == 0


def test_exponent():
    assert exponent(1, 2) == 1
    assert exponent(1, -2) == 1
    assert exponent(3, 3) == 27
    assert round(exponent(3, -3), 3) == 0.037


def test_subt():
    assert subt(1, 2) == -1
    assert subt(1, -2) == 3
    assert subt(3, 3) == 0
    assert subt(3, -3) == 6
