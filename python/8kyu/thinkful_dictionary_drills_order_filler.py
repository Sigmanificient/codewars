from typing import Dict


def fillable(stock: Dict[str, int], merch: str, n: int):
    """Kata url: https://www.codewars.com/kata/586ee462d0982081bf001f07."""
    return stock.get(merch, False) >= n
