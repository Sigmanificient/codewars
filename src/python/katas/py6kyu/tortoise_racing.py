from typing import List


def race(v1: int, v2: int, g: int) -> List[int]:
    if v1 >= v2:
        return None

    v1ps, v2ps = v1 / 3600, v2 / 3600
    a, b, s = g, 0, 0

    while a > b:
        a += v1ps
        b += v2ps
        s += 1

    r, s = divmod(s - (b - a > 0.0001), 60)
    return [*divmod(r, 60), s]


def test_race():
    assert race(720, 850, 70) == [0, 32, 18]
    assert race(80, 91, 37) == [3, 21, 49]
    assert race(820, 81, 550) is None
