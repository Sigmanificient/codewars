"""Kata url: https://www.codewars.com/kata/54f9173aa58bce9031001548."""
from typing import Callable, List


def take_while(arr: List[int], pred_fun: Callable[[int], bool]) -> List[int]:
    out = []
    for item in arr:
        if pred_fun(item):
            out.append(item)
        else:
            break
    return out


def test_take_while():
    is_even = lambda x: not x % 2
    is_odd = lambda x: not is_even(x)

    assert take_while([], is_even) == []
    assert take_while([2, 6, 4, 10, 1, 5, 4, 3], is_even) == [2, 6, 4, 10]
    assert take_while([2, 100, 1000, 10000, 5, 3, 4, 6], is_even) == [
        2,
        100,
        1000,
        10000,
    ]
    assert take_while([998, 996, 12, -1000, 200, 0, 1, 1, 1], is_even) == [
        998,
        996,
        12,
        -1000,
        200,
        0,
    ]
    assert take_while([1, 4, 2, 3, 5, 4, 5, 6, 7], is_even) == []
    assert take_while([2, 4, 10, 100, 64, 78, 92], is_even) == [
        2,
        4,
        10,
        100,
        64,
        78,
        92,
    ]
    assert take_while([1, 5, 111, 1111, 2, 4, 6, 4, 5], is_odd) == [1, 5, 111, 1111]
    assert take_while([-1, -5, 127, 86, 902, 2, 1], is_odd) == [-1, -5, 127]
    assert take_while([2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0], is_odd) == []
    assert take_while([1, 3, 5, 7, 9, 111], is_odd) == [1, 3, 5, 7, 9, 111]
