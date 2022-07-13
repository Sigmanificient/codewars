"""Kata url: https://www.codewars.com/kata/5c09ccc9b48e912946000157."""
from typing import List


def peak_height(mountain: List[str]) -> int:
    # TODO: optimize this in O(n²)
    old = []
    out = [
        [-1 for _i in range(len(mountain[0]))]
        for _j in range(len(mountain))
    ]

    for y, line in enumerate(mountain):
        for x, s in enumerate(line):
            if s == ' ':
                out[y][x] = 0
                continue

            out[y][x] = 1

    while old != out:
        old = [line[:] for line in out]

        for y, line in enumerate(mountain):
            for x, s in enumerate(line):
                n, s, e, w = 0, 0, 0, 0
                if s == ' ':
                    continue

                if y > 0:
                    n = out[y - 1][x]
                if y < len(out) - 1:
                    s = out[y + 1][x]
                if x > 0:
                    w = out[y][x - 1]
                if x < len(out[0]) - 1:
                    e = out[y][x + 1]

                if n > 0 and s > 0 and e > 0 and w > 0:
                    out[y][x] = min(n, s, e, w) + 1

    return max(max(line) for line in out)


def test_peak_height():
    assert peak_height(
        [
            "^^^^^^        ",
            " ^^^^^^^^     ",
            "  ^^^^^^^     ",
            "  ^^^^^       ",
            "  ^^^^^^^^^^^ ",
            "  ^^^^^^      ",
            "  ^^^^        "
        ]
    ) == 3
