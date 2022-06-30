"""Kata url: https://www.codewars.com/kata/56170e844da7c6f647000063."""

from typing import Dict

ages: Dict[int, str] = {
    13: "toddy",
    17: "coke",
    18: "beer",
    20: "beer",
    30: "whisky"
}


def people_with_age_drink(age: int) -> str:
    for d_age, drink in ages.items():
        if age <= d_age:
            return f"drink {drink}"

    return "drink toddy"


def test_people_with_age_drink():
    assert people_with_age_drink(13) == 'drink toddy'
    assert people_with_age_drink(0) == 'drink toddy'

    assert people_with_age_drink(17) == 'drink coke'
    assert people_with_age_drink(15) == 'drink coke'
    assert people_with_age_drink(14) == 'drink coke'

    assert people_with_age_drink(20) == 'drink beer'
    assert people_with_age_drink(18) == 'drink beer'

    assert people_with_age_drink(22) == 'drink whisky'
    assert people_with_age_drink(21) == 'drink whisky'
