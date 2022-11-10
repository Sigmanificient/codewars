"""Kata url: https://www.codewars.com/kata/5a092d9e46d843b9db000064."""


def solve(arr):
    for x in arr:
        if -x not in arr:
            return x
