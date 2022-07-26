"""Kata url: https://www.codewars.com/kata/5761a717780f8950ce001473."""


def calculate_age(year_of_birth: int, current_year: int) -> str:
    v: int = current_year - year_of_birth

    if not v:
        return "You were born this very year!"

    if v < 0:
        return f"You will be born in {abs(v)} year{'s' * (abs(v) > 1)}."

    return f"You are {v} year{'s' * (v > 1)} old."


def test_calculate_age():
    assert calculate_age(2012, 2016) == "You are 4 years old."
    assert calculate_age(1989, 2016) == "You are 27 years old."
    assert calculate_age(2000, 2090) == "You are 90 years old."
    assert calculate_age(2000, 1990) == "You will be born in 10 years."
    assert calculate_age(2000, 2000) == "You were born this very year!"
    assert calculate_age(900, 2900) == "You are 2000 years old."
    assert calculate_age(2010, 1990) == "You will be born in 20 years."
    assert calculate_age(2010, 1500) == "You will be born in 510 years."
    assert calculate_age(2011, 2012) == "You are 1 year old."
    assert calculate_age(2000, 1999) == "You will be born in 1 year."
