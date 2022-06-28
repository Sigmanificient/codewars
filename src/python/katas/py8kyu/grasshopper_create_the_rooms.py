"""Kata url: https://www.codewars.com/kata/56a29b237e9e997ff2000048."""

from typing import Dict

rooms: Dict[str, Dict[str, str]] = {
    '1': {
        'name': '...',
        'description': '...',
        'completed': '...'
    },
    '2': {
        'name': '...',
        'description': '...',
        'completed': '...'
    },
    '3': {
        'name': '...',
        'description': '...',
        'completed': '...'
    }
}


def test_solution():
    assert len(rooms) >= 3

    for name in rooms.values():
        assert isinstance(name, dict)

    for name in rooms.values():
        assert len(name) >= 3
