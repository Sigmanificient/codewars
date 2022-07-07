"""Kata url: https://www.codewars.com/kata/610c8308ed5ee4003279d112."""

from typing import Dict


def snake_case(string) -> str:
    return ''.join(
        char if char.islower() else f'_{char.lower()}'
        for char in string
    )


def snake_casify(dictionary) -> Dict[str, str]:
    return {
        snake_case(k): v for k, v in dictionary.items()
    }
