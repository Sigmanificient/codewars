"""Kata url: https://www.codewars.com/kata/514a6336889283a3d2000001."""


def get_even_numbers(arr):
    return [x for x in arr if not x & 1]


def test_get_even_numbers():
    assert get_even_numbers([2, 4, 5, 6]) == [2, 4, 6]
    assert get_even_numbers([]) == []
    assert get_even_numbers([1]) == []
    assert get_even_numbers([1, 2]) == [2]
    assert get_even_numbers([1, 2, 3, 4, 5]) == [2, 4]
    assert get_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]
