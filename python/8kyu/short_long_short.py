"""Kata url: https://www.codewars.com/kata/50654ddff44f800200000007."""


def solution(a, b):
    if len(a) > len(b):
        a, b = b, a

    return f"{a}{b}{a}"
