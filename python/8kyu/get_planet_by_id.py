from typing import Tuple

planets: Tuple[str, ...] = (
    "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
)


def get_planet_name(_id: int) -> str:
    """Kata url: https://www.codewars.com/kata/515e188a311df01cba000003."""
    return planets[_id - 1]
