"""Kata url: https://www.codewars.com/kata/62d34faad32b8c002a17d6d9."""
from typing import List


def fifo(n: int, reference_list: List[int]) -> List[int]:
    memory = [-1] * n
    c = 0

    for ref in reference_list:
        if ref in memory:
            continue

        memory[c] = ref
        c = (c + 1) % n

    return memory


def test_fifo():
    assert fifo(3, [1, 2, 3, 4, 2, 5]) == [4, 5, 3]
    assert fifo(5, []) == [-1, -1, -1, -1, -1]
    assert fifo(4, [1, 2, 3, 3, 4, 5, 1]) == [5, 1, 3, 4]
    assert fifo(4, [1, 1, 1, 2, 2, 3]) == [1, 2, 3, -1]
    assert fifo(1, [5, 4, 3, 3, 4, 10]) == [10]
    assert fifo(3, [1, 1, 1, 1, 1, 1, 1, 1]) == [1, -1, -1]
    assert fifo(
        5, [10, 9, 8, 7, 7, 8, 7, 6, 5, 4, 3, 4, 3, 4, 5, 6, 5]
    ) == [5, 4, 3, 7, 6]
