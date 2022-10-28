"""Kata url: https://www.codewars.com/kata/55a4f1f67157d8cbe200007b."""
from dataclasses import dataclass
from typing import List


@dataclass
class World:
    map: List[List[int]]

    def __post_init__(self):
        self.height = len(self.map)
        self.width = len(self.map[0])

    def claim_island(self, x: int, y: int, c: int) -> bool:
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        if self.map[y][x] != 'x':
            return False

        self.map[y][x] = str(c)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            self.claim_island(x - dx, y - dy, c)

        return True


def count_islands(image: List[List[int]]) -> int:
    if not image or not image[0]:
        return 0

    count = 0
    world = World(image)

    for y, world_line in enumerate(world.map):
        for x, cell in enumerate(world_line):
            count += world.claim_island(x, y, count)

    return count
