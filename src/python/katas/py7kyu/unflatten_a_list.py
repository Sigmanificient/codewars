"""Kata url: https://www.codewars.com/kata/57e2dd0bec7d247e5600013a."""
from typing import List, Union


def unflatten(flat_array: List[int]) -> List[Union[int, List[int]]]:
    out = []
    flat_array = flat_array[::-1]

    while flat_array:
        n = flat_array.pop()

        if n < 3:
            out.append(n)

        if n > 2:
            n -= 1
            out.append([n + 1] + flat_array[-n:][::-1])
            flat_array = flat_array[:-n]

    return out


def test_unflatten():
    assert unflatten([3, 5, 2, 1]) == [[3, 5, 2], 1]
    assert unflatten([1, 4, 5, 2, 1, 2, 4, 5, 2, 6, 2, 3, 3]) == [
        1,
        [4, 5, 2, 1],
        2,
        [4, 5, 2, 6],
        2,
        [3, 3],
    ]

    assert unflatten([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert unflatten([1]) == [1]
    assert unflatten([99, 1, 1, 1]) == [[99, 1, 1, 1]]
    assert unflatten([3, 1, 1, 3, 1, 1]) == [[3, 1, 1], [3, 1, 1]]
