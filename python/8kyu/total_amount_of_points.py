from typing import List


def points(games: List[str]) -> int:
    """Kata url: https://www.codewars.com/kata/5bb904724c47249b10000131."""
    point: int = 0

    for match in games:
        y, x = match.split(':')

        if x == y:
            point += 1
            continue

        if x < y:
            point += 3

    return point
