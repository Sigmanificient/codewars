"""Kata url: https://www.codewars.com/kata/57cf50a7eca2603de0000090."""
from string import ascii_lowercase as alpha


def move_ten(st: str) -> str:
    return ''.join(
        alpha[(alpha.index(c) + 10) % 26]
        for c in st
    )


def test_move_ten():
    assert move_ten("testcase") == "docdmkco"
    assert move_ten("codewars") == "mynogkbc"
    assert move_ten("exampletesthere") == "ohkwzvodocdrobo"
    assert move_ten("returnofthespacecamel") == "bodebxypdroczkmomkwov"
    assert move_ten("bringonthebootcamp") == "lbsxqyxdrolyydmkwz"
    assert move_ten("weneedanofficedog") == "goxoonkxyppsmonyq"
