"""Kata url: https://www.codewars.com/kata/583203e6eb35d7980400002a."""

from typing import List


def count_smileys(arr: List[str]) -> int:
    return sum(
        (h in ":;" and f in ")D" and (not b or b[0] in "-~")) for h, *b, f in arr
    )


def test_count_smileys():
    assert count_smileys([]) == 0
    assert count_smileys([":D", ":~)", ";~D", ":)"]) == 4
    assert count_smileys([":)", ":(", ":D", ":O", ":;"]) == 2
    assert count_smileys([";]", ":[", ";*", ":$", ";-D"]) == 1
