"""Kata url: https://www.codewars.com/kata/59b401e24f98a813f9000026."""


def compute_depth(n):
    depth = 0
    found = set()

    while len(found) != 10:
        depth += 1
        x = n * depth

        found.update(set(map(int, str(x))))

    return depth


def test_compute_depth():
    assert compute_depth(1) == 10
    assert compute_depth(42) == 9
    assert compute_depth(8) == 12
    assert compute_depth(13) == 8
    assert compute_depth(7) == 10
    assert compute_depth(25) == 36
    assert compute_depth(42) == 9
    assert compute_depth(1) == 10
