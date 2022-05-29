"""Kata url: https://www.codewars.com/kata/592645498270ccd7950000b4."""


def typist(s: str) -> int:
    total: int = 0

    cap_lock: bool = False
    for char in s:
        if char.isupper() != cap_lock:
            cap_lock = not cap_lock
            total += 1

    return total + len(s)


def test_typist():
    sample_test_cases = (
        ('a', 1),
        ('aa', 2),
        ('A', 2),
        ('AA', 3),
        ('aA', 3),
        ('Aa', 4),
        ('BeiJingDaXueDongMen', 31),
        ('AAAaaaBBBbbbABAB', 21),
        ('AmericanRAILWAY', 18),
        ('AaAaAa', 12),
        ('DFjfkdaB', 11)
    )

    for s, expected in sample_test_cases:
        assert typist(s) == expected
