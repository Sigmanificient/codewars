"""Kata url: https://www.codewars.com/kata/56bb9b7838dd34d7d8001b3c."""

def flood(maze: list[str], visited: list[list[bool]], x: int, y: int) -> bool:
    if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
        return True

    if visited[y][x]:
        return False
    visited[y][x] = True
    return any(
        flood(maze, visited, x + dx, y + dy)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
    )


def has_exit(maze: list[str]) -> bool:
    if sum(line.count('k') for line in maze) != 1:
        raise ValueError

    pline = next((n for n, line in enumerate(maze) if 'k' in line), -1)
    if pline < 0:
        raise ValueError

    pcol = maze[pline].index('k')
    visited = [[cell == '#' for cell in line] for line in maze]
    return flood(maze, visited, pcol, pline)