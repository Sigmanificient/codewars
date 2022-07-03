"""Kata url: https://www.codewars.com/kata/577bd026df78c19bca0002c0."""


def correct(s: str) -> str:
    return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')


def test_correct():
    assert correct("L0ND0N") == "LONDON"
    assert correct("DUBL1N") == "DUBLIN"
    assert correct("51NGAP0RE") == "SINGAPORE"
    assert correct("BUDAPE5T") == "BUDAPEST"
    assert correct("PAR15") == "PARIS"
