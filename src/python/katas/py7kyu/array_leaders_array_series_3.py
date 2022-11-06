"""Kata url: https://www.codewars.com/kata/5a651865fd56cb55760000e0."""


def array_leaders(numbers):
    return [
        n for c, n in enumerate(numbers)
        if sum(numbers[c + 1:]) < n
    ]


def test_array_leaders():
    assert array_leaders([1, 2, 3, 4, 0]) == [4]
    assert array_leaders([16, 17, 4, 3, 5, 2]) == [17, 5, 2]
    assert array_leaders([-1, -29, -26, -2]) == [-1]
    assert array_leaders([-36, -12, -27]) == [-36, -12]
    assert array_leaders([5, 2]) == [5, 2]
    assert array_leaders([0, -1, -29, 3, 2]) == [0, -1, 3, 2]
