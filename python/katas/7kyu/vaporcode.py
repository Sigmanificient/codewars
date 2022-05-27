"""Kata url: https://www.codewars.com/kata/5966eeb31b229e44eb00007a."""


def vaporcode(s: str) -> str:
    return '  '.join(s.upper().replace(' ', ''))
