"""Kata url: https://www.codewars.com/kata/57f604a21bd4fe771b00009c."""
from typing import Union, List


def meeting(rooms: List[str]) -> Union[int, str]:
    return next(
        (idx for idx, room in enumerate(rooms) if room == 'O'),
        'None available!'
    )


def test_meeting():
    assert meeting(['X', 'O', 'X']) == 1
    assert meeting(['O', 'X', 'X', 'X', 'X']) == 0
    assert meeting(['X', 'X', 'O', 'X', 'X']) == 2
    assert meeting(['X']) == 'None available!'
