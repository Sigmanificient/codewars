"""Kata url: https://www.codewars.com/kata/58649884a1659ed6cb000072."""
from typing import List


lights: List[str] = ["green", "yellow", "red"]


def update_light(current: str) -> str:
    return lights[(lights.index(current) + 1) % len(lights)]


def test_update_light():
    assert update_light("green") == "yellow"
    assert update_light("yellow") == "red"
    assert update_light("red") == "green"
