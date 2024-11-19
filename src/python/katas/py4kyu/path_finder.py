"""Kata url: https://www.codewars.com/kata/5765870e190b1472ec0022a2."""


def flood(maze, target, visited, x, y):
    if (x, y) == target:
        return True, ()

    if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
        return False, ()

    if visited[y][x]:
        return False, ()

    visited[y][x] = True
    return False, [
        (x + dx, y + dy)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
    ]


def path_finder(maze_line):
    maze = maze_line.splitlines()

    width, height = len(maze[0]), len(maze)
    visited = [[c == 'W' for c in line] for line in maze]

    to_visit = [(0, 0)]
    while to_visit:
        found, v = flood(
            maze,
            (width - 1 , height - 1),
            visited,
            *to_visit.pop()
        )

        if found:
            return True

        to_visit.extend(v)
    return False