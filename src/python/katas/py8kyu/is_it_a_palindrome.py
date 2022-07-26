"""Kata url: https://www.codewars.com/kata/57a1fd2ce298a731b20006a4."""


def is_palindrome(s: str) -> bool:
    return s.lower() == s[::-1].lower()


def test_is_palindrome():
    assert is_palindrome("a")
    assert is_palindrome("aba")
    assert is_palindrome("Abba")
    assert is_palindrome("malam")
    assert is_palindrome("kodok")
    assert not is_palindrome("walter")
    assert not is_palindrome("Kasue")
