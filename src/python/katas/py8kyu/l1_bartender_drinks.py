"""Kata url: https://www.codewars.com/kata/568dc014440f03b13900001d."""

from typing import Dict

drinks: Dict[str, str] = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal",
}


def get_drink_by_profession(param: str) -> str:
    return drinks.get(param.lower(), "Beer")


def test_get_drink_by_profession():
    assert (
        get_drink_by_profession("jabrOni") == "Patron Tequila"
    ), "'Jabroni' should map to 'Patron Tequila'"
    assert (
        get_drink_by_profession("scHOOl counselor") == "Anything with Alcohol"
    ), "'School Counselor' should map to 'Anything with alcohol'"
    assert (
        get_drink_by_profession("prOgramMer") == "Hipster Craft Beer"
    ), "'Programmer' should map to 'Hipster Craft Beer'"
    assert (
        get_drink_by_profession("bike ganG member") == "Moonshine"
    ), "'Bike Gang Member' should map to 'Moonshine'"
    assert (
        get_drink_by_profession("poLiTiCian") == "Your tax dollars"
    ), "'Politician' should map to 'Your tax dollars'"
    assert (
        get_drink_by_profession("rapper") == "Cristal"
    ), "'Rapper' should map to 'Cristal'"
    assert get_drink_by_profession("pundit") == "Beer", "'Pundit' should map to 'Beer'"
    assert get_drink_by_profession("Pug") == "Beer", "'Pug' should map to 'Beer'"
