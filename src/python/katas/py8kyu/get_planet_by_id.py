"""Kata url: https://www.codewars.com/kata/515e188a311df01cba000003."""

from typing import Tuple

planets: Tuple[str, ...] = (
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
)


def get_planet_name(_id: int) -> str:
    return planets[_id - 1]


def test_get_planet_name():
    assert get_planet_name(2) == "Venus"
    assert get_planet_name(5) == "Jupiter"
    assert get_planet_name(3) == "Earth"
    assert get_planet_name(4) == "Mars"
    assert get_planet_name(8) == "Neptune"
    assert get_planet_name(1) == "Mercury"
