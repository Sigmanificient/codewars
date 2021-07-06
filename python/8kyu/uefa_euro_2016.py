from typing import List


def uefa_euro_2016(teams: List[str], scores: List[int]) -> str:
    """Kata url: https://www.codewars.com/kata/57613fb1033d766171000d60."""
    team_1, team_2 = teams
    won: str = "teams played draw." if scores[0] == scores[1] else f"{teams[scores[0] < scores[1]]} won!"
    return f"At match {team_1} - {team_2}, {won}"
