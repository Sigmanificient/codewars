"""Kata url: https://www.codewars.com/kata/575fa9afee048b293e000287."""
from typing import Union


def how_much_water(water, load, clothes) -> Union[float, str]:
    if load > clothes:
        return 'Not enough clothes'

    if clothes > 2 * load:
        return 'Too much clothes'

    return round(water * (1.1 ** abs(load - clothes)), 2)
