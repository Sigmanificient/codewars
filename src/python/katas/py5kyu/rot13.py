"""Kata url: https://www.codewars.com/kata/52223df9e8f98c7aa7000062."""

from string import ascii_lowercase

def _rot13_char(c):
    p = ascii_lowercase.find(c.lower())
    if p == -1:
        return c

    l = ascii_lowercase[(p + 13) % len(ascii_lowercase)]
    return l if c.islower() else l.upper()


def rot13(message):
    return ''.join(map(_rot13_char, message))