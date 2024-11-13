"""Kata url: https://www.codewars.com/kata/5b258cf6d74b5b7105000035."""

def flood(grid, x, y, target) -> int:
    if x < 0 or x >= len(grid[0]):
        return 0
    if y < 0 or y >= len(grid):
        return 0
    if grid[y][x] != target:
        return 0

    grid[y][x] = -1
    return 1 + sum(
        flood(grid, x + dx, y + dy, target)
        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1))
    )


def find_most_adjacent(grid):
    bv, bc = (-1, 0)

    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell == -1:
                continue

            count = flood(grid, x, y, cell)
            if count > bc:
                bv, bc = (cell, count)
            elif count == bc and cell < bv:
                bv = cell

    return bv, bc
