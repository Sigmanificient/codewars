"""Kata url: https://www.codewars.com/kata/5556282156230d0e5e000089."""


def dna_strand(dna: str) -> str:
    return dna.translate(dna.maketrans("ACGT", "TGCA"))


def test_dna_strand():
    assert dna_strand("AAAA") == "TTTT"
    assert dna_strand("ATTGC") == "TAACG"
    assert dna_strand("GTAT") == "CATA"
