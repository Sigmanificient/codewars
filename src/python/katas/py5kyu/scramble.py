"""Kata url: https://www.codewars.com/kata/55c04b4cc56a697bb0000048."""


def scramble(s1: str, s2: str) -> bool:
    return all(s1.count(x) >= s2.count(x) for x in sorted(set(s2)))


def test_scramble():
    assert scramble("rkqodlw", "world")
    assert scramble("cedewaraaossoqqyt", "codewars")
    assert not scramble("katas", "steak")
    assert scramble("scriptjava", "javascript")
    assert scramble("scriptingjava", "javascript")
