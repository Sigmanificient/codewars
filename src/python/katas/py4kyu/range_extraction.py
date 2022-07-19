"""Kata url: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f."""
from typing import List


def solution(args: List[int]) -> str:
    sub, seq = [args[0]], []

    for arg, nex in zip(args, args[1::]):
        if arg + 1 == nex:
            sub.append(nex)

        else:
            seq.append(sub)
            sub = [nex]

    seq.append(sub)

    return ','.join(
        f"{i[0]}-{i[-1]}" if len(i) > 2 else ','.join(map(str, i))
        for i in seq
    )


def test_solution():
    assert solution([1, 2, 3, 4, 5]) == '1-5'
    assert solution(
        [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
    ) == '-6,-3-1,3-5,7-11,14,15,17-20'
    assert solution(
        [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]
    ) == '-3--1,2,10,15,16,18-20'
