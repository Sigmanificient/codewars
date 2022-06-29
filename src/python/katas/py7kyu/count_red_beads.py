def count_red_beads(n: int) -> int:
    return max(0, (n - 1) * 2)


def test_count_red_beads():
    assert count_red_beads(0) == 0
    assert count_red_beads(1) == 0
    assert count_red_beads(3) == 4
    assert count_red_beads(5) == 8
