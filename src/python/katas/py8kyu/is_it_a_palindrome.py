"""Kata url: https://www.codewars.com/kata/57a1fd2ce298a731b20006a4."""


def is_palindrome(s: str) -> bool:
    return s.lower() == s[::-1].lower()
