from typing import Union


def is_palindrome(string: Union[str, int]) -> bool:
    """Kata url: https://www.codewars.com/kata/57a5015d72292ddeb8000b31."""
    string = str(string)
    return string == string[::-1]
