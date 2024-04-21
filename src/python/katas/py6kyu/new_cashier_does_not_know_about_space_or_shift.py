"""Kata url: https://www.codewars.com/kata/5d23d89906f92a00267bb83d."""
from typing import Dict, List

MENU = {
    647: "Burger",
    537: "Fries",
    725: "Chicken",
    558: "Pizza",
    849: "Sandwich",
    1094: "Onionrings",
    953: "Milkshake",
    418: "Coke",
}


def get_order(order: str) -> str:
    orders: Dict[str, int] = {k: 0 for k in MENU.values()}

    word = 0
    for char in order:
        word += ord(char)

        single_order: str = MENU.get(word, "")
        if order:
            orders[single_order] += 1
            word = 0

    out: List[str] = []
    for name, count in orders.items():
        out.extend([name] * count)

    return " ".join(out)


def test_get_order():
    assert get_order(
        "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
    ) == "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"

    assert (
        get_order("pizzachickenfriesburgercokemilkshakefriessandwich")
        == "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke"
    )