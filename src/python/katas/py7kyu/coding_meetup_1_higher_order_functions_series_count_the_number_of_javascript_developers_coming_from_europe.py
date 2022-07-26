"""Kata url: https://www.codewars.com/kata/582746fa14b3892727000c4f."""
from typing import List, Dict, Union


def count_developers(lst: List[Dict[str, Union[int, str]]]) -> int:
    return sum(
        True
        for x in lst
        if (x["continent"] == "Europe" and x["language"] == "JavaScript")
    )


def test_count_developers():
    assert (
        count_developers(
            [
                {
                    "firstName": "Oliver",
                    "lastName": "Q.",
                    "country": "Australia",
                    "continent": "Oceania",
                    "age": 19,
                    "language": "HTML",
                },
                {
                    "firstName": "Lukas",
                    "lastName": "R.",
                    "country": "Austria",
                    "continent": "Europe",
                    "age": 89,
                    "language": "HTML",
                },
            ]
        )
        == 0
    )

    assert (
        count_developers(
            [
                {
                    "firstName": "Noah",
                    "lastName": "M.",
                    "country": "Switzerland",
                    "continent": "Europe",
                    "age": 19,
                    "language": "JavaScript",
                },
                {
                    "firstName": "Maia",
                    "lastName": "S.",
                    "country": "Tahiti",
                    "continent": "Oceania",
                    "age": 28,
                    "language": "JavaScript",
                },
                {
                    "firstName": "Shufen",
                    "lastName": "L.",
                    "country": "Taiwan",
                    "continent": "Asia",
                    "age": 35,
                    "language": "HTML",
                },
                {
                    "firstName": "Sumayah",
                    "lastName": "M.",
                    "country": "Tajikistan",
                    "continent": "Asia",
                    "age": 30,
                    "language": "CSS",
                },
            ]
        )
        == 1
    )
