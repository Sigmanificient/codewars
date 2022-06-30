"""Kata url: https://www.codewars.com/kata/55b42574ff091733d900002f."""

from typing import List


def friend(x: List[str]) -> List[str]:
    return [f for f in x if len(f) == 4]


def test_friend():
    assert friend(["Ryan", "Kieran", "Mark", ]) == ["Ryan", "Mark"]
    assert friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]) == ["Ryan"]
    assert friend(
        ["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]
    ) == ["Jimm", "Cari", "aret"]
