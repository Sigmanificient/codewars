"""Kata url: https://www.codewars.com/kata/580435ab150cca22650001fb."""


def filter_lucky(lst):
    return [x for x in lst if '7' in str(x)]


def test_filter_lucky():
    assert filter_lucky([7]) == [7]
    assert filter_lucky([1, 2, 3]) == []
    assert filter_lucky([77, 8]) == [77]
    assert filter_lucky([71]) == [71]
    assert filter_lucky([71, 9907, 69]) == [71, 9907]
