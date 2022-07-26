"""Kata url: https://www.codewars.com/kata/56ff1667cc08cacf4b00171."""
from collections import Counter


VEGETABLES = [
    "cabbage",
    "carrot",
    "celery",
    "cucumber",
    "mushroom",
    "onion",
    "pepper",
    "potato",
    "tofu",
    "turnip",
]


def count_vegetables(string):
    return sorted(
        [(v, k) for k, v in Counter(string.split()).items() if k in VEGETABLES],
        reverse=True,
    )
