"""Kata url: https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e."""


def sum_of_differences(arr):
    arr = sorted(arr, reverse=True)
    return sum(abs(x - y) for x, y in zip(arr, arr[1:]))


def test_sum_of_differences():
    assert sum_of_differences([1, 2, 10]) == 9
    assert sum_of_differences([-3, -2, -1]) == 2
    assert sum_of_differences([1, 1, 1, 1, 1]) == 0
    assert sum_of_differences([-17, 17]) == 34
    assert sum_of_differences([]) == 0
    assert sum_of_differences([0]) == 0
    assert sum_of_differences([-1]) == 0
    assert sum_of_differences([1]) == 0
