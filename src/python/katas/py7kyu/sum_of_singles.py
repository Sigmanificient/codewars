"""Kata url: https://www.codewars.com/kata/59f11118a5e129e591000134."""


def repeats(arr):
    found = set()
    total = 0

    for i in arr:
        if i in found:
            total -= i
        else:
            total += i

        found.add(i)

    return total


def test_repeats():
    assert repeats([4, 5, 7, 5, 4, 8]) == 15
    assert repeats([9, 10, 19, 13, 19, 13]) == 19
    assert repeats([16, 0, 11, 4, 8, 16, 0, 11]) == 12
    assert repeats([5, 17, 18, 11, 13, 18, 11, 13]) == 22
    assert repeats([5, 10, 19, 13, 10, 13]) == 24
