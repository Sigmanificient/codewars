"""Kata url: https://www.codewars.com/kata/559590633066759614000063."""


def min_max(lst):
    return [min(lst), max(lst)]


def test_min_max():
    assert min_max([1, 2, 3, 4, 5]) == [1, 5]
    assert min_max([2334454, 5]) == [5, 2334454]
