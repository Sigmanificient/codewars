"""Kata url: https://www.codewars.com/kata/57cff961eca260b71900008f."""


from typing import Union, List


def is_vow(inp: List[Union[int, str]]) -> List[Union[int, str]]:
    buf: List[Union[int, str]] = []
    for x in inp:
        letter: str = chr(x) if isinstance(x, int) else x

        if letter in 'aeiou':
            buf.append(letter)

        else:
            buf.append(x)

    return buf
