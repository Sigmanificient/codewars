"""Kata url: https://www.codewars.com/kata/5a4138acf28b82aa43000117."""


def adjacent_element_product(array):
    return max(a * b for a, b in zip(array, array[1::]))


def test_adj_element_product():
    assert adjacent_element_product([5, 8]) == 40
    assert adjacent_element_product([1, 2, 3]) == 6
    assert adjacent_element_product([1, 5, 10, 9]) == 90
    assert adjacent_element_product([4, 12, 3, 1, 5]) == 48
    assert adjacent_element_product([5, 1, 2, 3, 1, 4]) == 6
