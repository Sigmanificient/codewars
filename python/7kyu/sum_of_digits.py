# Kata url: https://www.codewars.com/kata/59cf805aaeb28438fe00001c.

from typing import Optional, Union


def sum_of_digits(digits: Optional[Union[int, str]]) -> str:
    if digits is None:
        return ''

    digits: str = str(digits)
    return ' + '.join(digits) + f" = {sum(map(int, digits))}"
