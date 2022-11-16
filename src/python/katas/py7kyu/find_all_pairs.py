"""Kata url: https://www.codewars.com/kata/5c55ad8c9d76d41a62b4ede3."""


def duplicates(arr):
    return sum(arr.count(x) // 2 for x in set(arr))


def test_duplicate():
    assert duplicates([1, 2, 5, 6, 5, 2]) == 2
    assert duplicates([1, 2, 2, 20, 6, 20, 2, 6, 2]) == 4
    assert duplicates([0, 0, 0, 0, 0, 0, 0]) == 3
    assert duplicates([1000, 1000]) == 1
    assert duplicates([]) == 0
    assert duplicates([54]) == 0
