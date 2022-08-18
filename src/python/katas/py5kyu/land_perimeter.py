"""Kata url: https://www.codewars.com/kata/5839c48f0cf94640a20001d3."""
from typing import List


def count_empty_neighbours(arr: List[str], x: int, y: int) -> int:
    height = len(arr)
    width = len(arr[0])

    count = 0

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        cx = x + dx

        if cx < 0 or cx >= width:
            count += 1
            continue

        cy = y + dy
        if cy < 0 or cy >= height:
            count += 1
            continue

        if arr[cy][cx] == 'O':
            count += 1
    return count


def land_perimeter(arr: List[str]) -> str:
    perimeter = 0
    for y, line in enumerate(arr):
        for x, cell in enumerate(line):
            if cell == 'O':
                continue

            perimeter += count_empty_neighbours(arr, x, y)

    return f"Total land perimeter: {perimeter}"


def test_land_perimeter():
    assert land_perimeter(
        [
            "OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO",
            "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO",
            "OXOOOO", "OXOOXX"
        ]
    ) == "Total land perimeter: 60"

    assert land_perimeter(
        [
            "OXOOO", "OOXXX", "OXXOO", "XOOOO",
            "XOOOO", "XXXOO", "XOXOO", "OOOXO",
            "OXOOX", "XOOOO", "OOOXO"
        ]
    ) == "Total land perimeter: 52"

    assert land_perimeter(
        ["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]
    ) == "Total land perimeter: 40"

    assert land_perimeter(
        [
            "XOOOXOO", "OXOOOOO", "XOXOXOO",
            "OXOXXOO", "OOOOOXX", "OOOXOXX",
            "XXXXOXO"
        ]
    ) == "Total land perimeter: 54"

    assert land_perimeter(
        [
            "OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO",
            "OOOOOO", "OOOXOO", "OOXXOO"
        ]
    ) == "Total land perimeter: 40"
