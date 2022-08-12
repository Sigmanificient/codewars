"""Kata url: https://www.codewars.com/kata/57b988048f5813799600004f."""
from typing import List


Matrix = List[List[int]]


def get_neighbour_count(cells: Matrix, y: int, x: int) -> int:
    lc_y = len(cells)
    lc_x = len(cells[0])

    neighbour_count = 0

    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == dy == 0:
                continue

            c_y = (y + dy) % lc_y
            c_x = (x + dx) % lc_x

            neighbour_count += cells[c_y][c_x]

    return neighbour_count


def get_next_gen(cells: Matrix) -> Matrix:
    out = [[0] * len(cells[0]) for _ in range(len(cells))]

    for y, line in enumerate(cells):
        for x, cell in enumerate(line):
            count = get_neighbour_count(cells, y, x)
            out[y][x] = int((2 <= count <= 3) if cell else (count == 3))

    return out


def get_generation(cells: Matrix, generation: int) -> Matrix:
    for _ in range(generation):
        cells = get_next_gen(cells)

    return cells


def test_get_generation():
    glider = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    assert get_generation(glider, 4) == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1]
    ]

    assert get_generation(glider, 12) == [
        [0, 1, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ]

    assert get_generation(glider, 16) == [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
