"""Kata url: https://www.codewars.com/kata/575fa9afee048b293e000287."""
from typing import Union


def how_much_water(water, load, clothes) -> Union[float, str]:
    if load > clothes:
        return "Not enough clothes"

    if clothes > 2 * load:
        return "Too much clothes"

    return round(water * (1.1 ** abs(load - clothes)), 2)


def test_how_much_water():
    assert how_much_water(10, 10, 21) == "Too much clothes"
    assert how_much_water(10, 10, 2) == "Not enough clothes"

    r = how_much_water(10, 11, 20)
    assert isinstance(r, float) and (r - 23.58) < 0.001

    r = how_much_water(50, 15, 29)
    assert isinstance(r, float) and (r - 189.87) < 0.001