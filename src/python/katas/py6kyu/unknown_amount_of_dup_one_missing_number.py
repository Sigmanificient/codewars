"""Kata url: https://www.codewars.com/kata/5a5cdb07fd56cbdd3c00005b."""
from typing import List, Union


def find_dups_miss(arr: List[int]) -> List[Union[int, List[int]]]:
    arr_set = set(arr)
    mn = mx = arr[0]

    visited = set()
    dups = set()

    for element in arr:
        if element > mx:
            mx = element

        elif element < mn:
            mn = element

        if element in visited:
            dups.add(element)
        else:
            visited.add(element)

    numbers = set(range(mn, mx + 1))
    for item in arr_set:
        numbers.remove(item)

    return [numbers.pop(), sorted(dups)]


def test_find_dups_miss():
    arr1 = [10, 9, 8, 9, 6, 1, 2, 4, 3, 2, 5, 5, 3]
    assert find_dups_miss(arr1) == [7, [2, 3, 5, 9]]

    assert find_dups_miss(
        [
            20, 19, 6, 9, 7, 17, 16, 17, 12,
            5, 6, 8, 9, 10, 14, 13, 11, 14, 15, 19
        ]
    ) == [18, [6, 9, 14, 17, 19]]

    assert find_dups_miss(
        [
            24, 25, 34, 40, 38, 26, 33, 29, 50, 31, 33, 56, 35, 36, 53,
            49, 57, 27, 37, 40, 48, 44, 32, 35, 45, 52, 43, 47, 26, 51,
            55, 28, 41, 42, 46, 51, 25, 30, 44, 54
        ]
    ) == [39, [25, 26, 33, 35, 40, 44, 51]]
