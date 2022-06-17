"""Kata url: https://www.codewars.com/kata/5861d28f124b35723e00005."""


def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    return distance_to_pump <= mpg * fuel_left


def test_zero_fuel():
    assert zero_fuel(50, 25, 2)
    assert zero_fuel(100, 50, 2)
    assert zero_fuel(25, 100, 2)

    assert not zero_fuel(100, 25, 2)
    assert not zero_fuel(6, 6, 0)
