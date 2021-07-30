"""Kata url: https://www.codewars.com/kata/586ee462d0982081bf001f07."""

from typing import Dict


def fillable(stock: Dict[str, int], merch: str, n: int):
    return stock.get(merch, False) >= n
