from typing import Union, List


def is_vow(inp: List[Union[int, str]]) -> List[Union[int, str]]:
    """Kata url: https://www.codewars.com/kata/57cff961eca260b71900008f."""
    return [chr(x) if (chr(x) if isinstance(x, int) else x) in 'aeiou' else x for x in inp]
