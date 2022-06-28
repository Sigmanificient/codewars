"""Kata url: https://www.codewars.com/kata/586c1cf4b98de0399300001d."""


def combat(health, damage):
    return max(0, health - damage)


def test_combat():
    assert combat(100, 5) == 95
    assert combat(83, 16) == 67
    assert combat(50, 10) == 40

    assert combat(20, 30) == 0
    assert combat(10, 10) == 0
    assert combat(0, 10) == 0
