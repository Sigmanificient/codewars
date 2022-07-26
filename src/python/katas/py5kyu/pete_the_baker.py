"""Kata url: https://www.codewars.com/kata/525c65e51bf619685c000059."""
from typing import Dict


def cakes(recipe: Dict[str, int], available: Dict[str, int]) -> int:
    p = []

    for k, v in recipe.items():
        if n := available.get(k):
            p.append(n // v)

        else:
            return 0

    return min(p)


def test_cakes():
    assert (
        cakes(
            {"flour": 500, "sugar": 200, "eggs": 1},
            {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
        )
        == 2
    )

    assert (
        cakes(
            {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
            {"sugar": 500, "flour": 2000, "milk": 2000},
        )
        == 0
    )
