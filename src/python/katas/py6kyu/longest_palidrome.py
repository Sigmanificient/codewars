"""Kata url: https://www.codewars.com/kata/54bb6f887e5a80180900046b."""


def longest_palindrome(s: str) -> int:
    max_p = 1 * bool(len(s))
    for off in range(2, len(s) + 1):
        for i in range(len(s) - off + 1):
            x = s[i:off + i]
            if x == x[::-1]:
                max_p = off
                break

    return max_p


def test_longest_palindrome():
    assert longest_palindrome("a") == 1
    assert longest_palindrome("aa") == 2
    assert longest_palindrome("baa") == 2
    assert longest_palindrome("aab") == 2
    assert longest_palindrome("abcdefghba") == 1
    assert longest_palindrome("baablkj12345432133d") == 9
