"""Kata url: https://www.codewars.com/kata/556196a6091a7e7f58000018."""


def largest_pair_sum(numbers):
    k = max(numbers)
    numbers.remove(k)
    return max(numbers) + k


def test_largest_pair_sum():
    assert largest_pair_sum([10, 14, 2, 23, 19]) == 42
    assert largest_pair_sum([-100, -29, -24, -19, 19]) == 0
    assert largest_pair_sum([1, 2, 3, 4, 6, -1, 2]) == 10
    assert largest_pair_sum([-10, -8, -16, -18, -19]) == -18
