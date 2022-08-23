"""Kata url: https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2."""


def sum_no_duplicates(lst):
    return sum(x for x in set(lst) if lst.count(x) < 2)


def test_sum_no_duplicates():
    assert sum_no_duplicates([1, 1, 2, 3]) == 5
    assert sum_no_duplicates([1, 1, 2, 2, 3]) == 3
