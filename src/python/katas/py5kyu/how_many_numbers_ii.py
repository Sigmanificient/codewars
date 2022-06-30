"""Kata url: https://www.codewars.com/kata/55f5efd21ad2b48895000040."""
from typing import List


def max_sum_dig(n: int, m: int) -> List[int]:
    digs = []
    for i in range(1000, n + 1):
        str_i = str(i)
        off_max = len(str_i) - 4

        for j in range(0, off_max + 1):
            s = sum(map(int, str_i[j: j + 4]))

            if s > m:
                break
        else:
            digs.append(i)

    mean = int((total := sum(digs)) / (n_digs := len(digs)))
    closest, min_diff = 0, 2 << 16

    for d in digs:
        if (diff := abs(mean - d)) <= min_diff:
            closest = d
            min_diff = diff

    return [n_digs, closest, total]


def test_max_sum_dig():
    assert max_sum_dig(2000, 3) == [11, 1110, 12555]
    assert max_sum_dig(2000, 4) == [21, 1120, 23665]
    assert max_sum_dig(2000, 7) == [85, 1200, 99986]
    assert max_sum_dig(3000, 7) == [141, 1600, 220756]
    assert max_sum_dig(4000, 4) == [35, 2000, 58331]
