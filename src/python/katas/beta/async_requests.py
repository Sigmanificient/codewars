"""Kata url: https://www.codewars.com/kata/62c702489012c30017ded374"""
import asyncio
from copy import copy
from itertools import cycle
from random import randint
from string import ascii_letters
from time import perf_counter

_cycler = cycle(ascii_letters)


async def _send_request():
    return (res := next(_cycler)) and await asyncio.sleep(0.2) or res


async def request_manager(n: int) -> str:
    return ''.join(await asyncio.gather(*(_send_request() for _ in range(n))))


def test_request_manager():
    _cycler_copy = copy(_cycler)

    def run_it(n: int) -> str:
        return asyncio.run(asyncio.wait_for(request_manager(n), 0.5))

    marker = perf_counter()

    for _ in range(5):
        rand = randint(14, 300)
        s = ''.join(next(_cycler_copy) for i in range(rand))
        assert run_it(rand) == s

    assert perf_counter() - marker < 3
