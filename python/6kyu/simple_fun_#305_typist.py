"""Kata url: https://www.codewars.com/kata/592645498270ccd7950000b4."""


def typist(s: str) -> int:
    total: int = 0

    cap_lock: bool = False
    for char in s:
        if char.isupper() != cap_lock:
            cap_lock = not cap_lock
            total += 1

    return total + len(s)
