"""Kata url: https://www.codewars.com/kata/568dc014440f03b13900001d."""

from typing import Dict

drinks: Dict[str, str] = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal"
}


def get_drink_by_profession(param: str) -> str:
    return drinks.get(param.lower(), "Beer")
