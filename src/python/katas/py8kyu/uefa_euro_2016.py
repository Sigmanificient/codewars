"""Kata url: https://www.codewars.com/kata/57613fb1033d766171000d60."""


from typing import List


def uefa_euro_2016(teams: List[str], scores: List[int]) -> str:
    team_1, team_2 = teams
    won: str = (
        "teams played draw."
        if scores[0] == scores[1] else f"{teams[scores[0] < scores[1]]} won!"
    )
    return f"At match {team_1} - {team_2}, {won}"


def test_uefa_euro_2016():
    assert uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]) == "At match Germany - Ukraine, Germany won!";
    assert uefa_euro_2016(['Belgium', 'Italy'], [0, 2]) == "At match Belgium - Italy, Italy won!"
    assert uefa_euro_2016(['Portugal', 'Iceland'], [1, 1]) == "At match Portugal - Iceland, teams played draw."
    assert uefa_euro_2016(['Albania', 'Switzerland'], [1, 2]) == "At match Albania - Switzerland, Switzerland won!"
    assert uefa_euro_2016(['Republic of Ireland', 'Sweden'], [0, 0]) == "At match Republic of Ireland - Sweden, teams played draw."
