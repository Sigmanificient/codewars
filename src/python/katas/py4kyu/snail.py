"""Kata url: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1."""

DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def snail(snail_map):
    collect = []
    cdir = 0

    height = len(snail_map)
    width = len(snail_map[0])

    x, y = (-1, 0)
    count = height * width
    i = 0

    while i < count:
        dx, dy = DIRS[cdir & 3]
        px = dx + x
        py = dy + y

        if (
            px < 0 or px >= width
            or py < 0 or py >= height
            or snail_map[py][px] == -1
        ):
            cdir += 1
            continue

        collect.append(snail_map[py][px])
        snail_map[py][px] = -1
        x, y = px, py
        i += 1
    return collect