"""Kata url: https://www.codewars.com/kata/586ee462d0982081bf001f07."""

from typing import Dict


def fillable(stock: Dict[str, int], merch: str, n: int):
    return stock.get(merch, False) >= n


def test_fillable():
    stock = {
        'football': 4,
        'boardgame': 10,
        'leggos': 1,
        'doll': 5
    }

    assert fillable(stock, 'football', 3)
    assert not fillable(stock, 'leggos', 2)
    assert not fillable(stock, 'action figure', 1)
