"""Kata url: https://www.codewars.com/kata/52423db9add6f6fc39000354."""
def get_cell(cells, x, y) -> int:
    nh_count = 0

    for dy, dx in (
      (-1, -1), (-1, 0), (-1, 1),
      (0, -1), (0, 1),
      (1, -1), (1, 0), (1, 1)
    ):
        cx = dx + x
        cy = dy + y

        if cx < 0 or cy < 0:
            continue
        if cx >= len(cells[0]) or cy >= len(cells):
            continue

        nh_count += cells[cy][cx] == 1

    alive = (
        x >= 0
        and y >= 0
        and x < len(cells[0])
        and y < len(cells)
        and cells[y][x] == 1
    )

    if not alive and nh_count == 3:
        return 1

    if nh_count < 2 or nh_count > 3:
        return 0

    return alive


def resize_view(out, height, width):
    sx = 0
    while sum(out[i][sx] for i in range(height)) == 0:
        sx += 1

    srx = width - 1
    while sum(out[i][srx] for i in range(height)) == 0:
        srx -= 1

    out = [line[sx:srx + 1] for line in out]

    sy = 0
    while sum(out[sy]) == 0:
        sy += 1

    sry = height - 1
    while sum(out[sry]) == 0:
        sry -= 1

    return out[sy:sry + 1]


def get_generation(cells : list[list[int]], generations : int) -> list[list[int]]:
    while generations:
        height = len(cells)
        width = len(cells[0])

        out = [[0 for _ in range(width + 2) ] for _ in range(height + 2)]

        for y in range(height + 2):
            for x in range(width + 2):
                out[y][x] = int(get_cell(cells, x - 1, y - 1))

        generations -= 1
        cells = resize_view(out, height + 2, width + 2)
    return cells