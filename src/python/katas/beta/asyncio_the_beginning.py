"""Kata url: https://www.codewars.com/kata/62cc8badb88fb2b0c4d09937."""
import asyncio
from time import perf_counter

import pytest


async def dreaming(n: float, m: int) -> float:
    await asyncio.sleep(n)
    return m**n


@pytest.mark.asyncio
async def test_dreaming():
    t = perf_counter()
    results = await asyncio.gather(*[dreaming(0.01, i) for i in range(10)])
    assert results == [k**0.01 for k in range(10)]
    assert perf_counter() - t < 0.03
