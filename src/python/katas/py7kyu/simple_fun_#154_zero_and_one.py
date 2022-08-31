"""Kata url: https://www.codewars.com/kata/58ad09d6154165a1c80000d1."""


def zero_and_one(s):
    count = i = 0
    length = len(s) - 1

    while i < length:
        if s[i] != s[i + 1]:
            i += 2
            continue

        count += 1
        i += 1

    return count + (i == length)


def test_zero_and_one():
    assert zero_and_one("01010") == 1
    assert zero_and_one("11101111") == 6
    assert zero_and_one("01") == 0
    assert zero_and_one("10") == 0
    assert zero_and_one("110110") == 2
    assert zero_and_one("110100") == 2
