"""Kata url: https://www.codewars.com/kata/57a5015d72292ddeb8000b31."""


from typing import Union


def is_palindrome(string: Union[str, int]) -> bool:
    string = str(string)
    return string == string[::-1]


def test_is_palindrome():
    assert is_palindrome("anna")
    assert not is_palindrome("walter")
    assert is_palindrome(12321)
    assert not is_palindrome(123456)
