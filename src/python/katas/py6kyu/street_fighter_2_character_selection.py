"""Kata url: https://www.codewars.com/kata/5853213063adbd1b9b0000be."""
from typing import List, Tuple


def street_fighter_selection(
        fighters: List[str],
        initial_position: Tuple[int, int],
        moves: List[str]
) -> List[str]:
    if not moves:
        return []

    y, x = initial_position

    directions = {
        'left': (-1, 0),
        'right': (1, 0),
        'up': (0, -1),
        'down': (0, 1)
    }

    mx, my = fighters[0], len(fighters) - 1
    hovered = []

    for move in moves:
        dx, dy = directions[move]

        x = (dx + x) % len(mx)
        y = min(max(y + dy, 0), my)

        hovered.append(fighters[y][x])

    return hovered


def test_street_fighter_selection():
    fighters = [
        ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
        ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
    ]

    assert street_fighter_selection(fighters, (0, 0), []) == []
    assert street_fighter_selection(fighters, (0, 0), ["left"] * 8) == [
        'Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog'
    ]

    assert street_fighter_selection(fighters, (0, 0), ["right"] * 8) == [
        'E.Honda', 'Blanka', 'Guile',
        'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka'
    ]

    assert street_fighter_selection(
        fighters, (0, 0), ["up"] * 4
    ) == ['Ryu', 'Ryu', 'Ryu', 'Ryu']

    assert street_fighter_selection(
        fighters, (0, 0), ["down"] * 4
    ) == ['Ken', 'Ken', 'Ken', 'Ken']

    assert street_fighter_selection(
        fighters, (0, 0), ["down", "right", "up", "left"] * 2
    ) == [
        'Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu'
    ]

    assert street_fighter_selection(
        fighters, (0, 0), ["up", "left", "down", "right"] * 2
    ) == ['Ryu', 'Vega', 'M.Bison', 'Ken', 'Ryu', 'Vega', 'M.Bison', 'Ken']

    assert street_fighter_selection(
        fighters, (0, 0), ["up"] + ["left"] * 6 + ["down"] + ["right"] * 6
    ) == [
        'Ryu', 'Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Ken',
        'Chun Li', 'Zangief', 'Dhalsim', 'Sagat', 'M.Bison', 'Ken'
    ]
