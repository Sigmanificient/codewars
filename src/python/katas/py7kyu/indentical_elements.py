"""Kata url: https://www.codewars.com/kata/583ebb9328a0c034490001ba."""


def duplicate_elements(m, n):
    return len(set(m + n)) != (len(set(n)) + len(set(m)))


def test_duplicate_elements():
    assert duplicate_elements([1, 2, 3, 4, 5], [1, 6, 7, 8, 9])
    assert duplicate_elements([9, 8, 7], [8, 1, 3])
    assert duplicate_elements([-2, -4, -6, -8], [-2, -3, -5, -7])
    assert duplicate_elements([-9, -8, -7], [-8, -1, -3])
