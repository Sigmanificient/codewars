"""Kata url: https://www.codewars.com/kata/54162d1333c02486a700011d."""

penultimate = lambda x: x[-2]


def test_penultimate():
    assert penultimate([1, 2, 3, 4]) ==  3
    assert penultimate("Python is dynamic") == 'i'
    assert penultimate("hello") == 'l'
