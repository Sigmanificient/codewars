"""Kata url: https://www.codewars.com/kata/5ec970f05864da001853b55b."""

from math import factorial
from typing import Callable, Dict


def memoized(func: Callable[[int], int]) -> Callable[[int], int]:
    cache: Dict[int, int] = {}

    def inner(k: int) -> int:
        v = cache.get(k)
        if v:
            return v

        v = func(k)
        cache[k] = v
        return v

    return inner


fac = memoized(factorial)


@memoized
def fof(n: int) -> int:
    t = 1
    for i in range(1, n + 1):
        t *= fac(i)

    return t


def test_fof():
    assert fof(4) == 288
    assert fof(1) == 1
    assert fof(5) == 34560
    assert fof(4) == 288
    assert fof(1) == 1
    assert fof(5) == 34560
    assert fof(2) == 2
    assert fof(6) == 24883200
    assert fof(3) == 12
    assert fof(8) == 5056584744960000
    assert fof(10) == 6658606584104736522240000000
    assert fof(9) == 1834933472251084800000
    assert fof(13) == 792786697595796795607377086400871488552960000000000000

    assert fof(25) == int(
        "1820828181018865827632761425264341519339479374506060689042961899219328"
        "3129810291626991262221974029109363817787141461966252773116546051694612"
        "7704699602179330129133022747131181054357741922910067575709873047846518"
        "78400000000000000000000000000000000000000000000000000000000"
    )
