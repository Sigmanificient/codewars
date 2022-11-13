"""Kata url: https://www.codewars.com/kata/5a0178f66f793bc5b0001728."""
from collections import Counter


def longest_palindrome(s):
    c = Counter(s.lower())
    total = one = 0

    for char, count in c.items():
        if not char.isalnum():
            continue

        print(char, count)
        if count & 1:
            count -= 1
            one += 1
        total += count
    return total + bool(one)


def test_longest_palindrome():
    assert longest_palindrome("A") == 1
    assert longest_palindrome("Hannah") == 6
    assert longest_palindrome("xyz__a_/b0110//a_zyx") == 13
    assert longest_palindrome("$aaabbbccddd_!jJpqlQx_.///yYabababhii_") == 25
    assert longest_palindrome("") == 0
