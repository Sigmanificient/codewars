from __future__ import annotations

from dataclasses import dataclass

import pytest
import requests
from bs4 import BeautifulSoup

URL = "https://www.codewars.com/users/leaderboard"


class OneIndexedList(list):
    def __getitem__(self, index):
        return super().__getitem__(index - 1)


@dataclass
class Leaderboard:
    position: OneIndexedList


@dataclass
class User:
    name: str
    clan: str
    honor: int


def solution():
    soup = BeautifulSoup(requests.get(URL).text, "html.parser")
    return Leaderboard(
        OneIndexedList(
            User(
                x.parent['data-username'],
                x.previous_element.text,
                int(x.text.replace(',', ''))
            )
            for x in soup.find_all('td', class_="honor")
        )
    )


def test_solution():
    leaderboard = solution()

    assert len(leaderboard.position) == 500

    assert leaderboard.position[1].name
    assert all(
        isinstance(u.honor, int)
        for u in leaderboard.position
    )
