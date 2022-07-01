"""Kata url: https://www.codewars.com/kata/5556282156230d0e5e000089."""


def dna_to_rna(dna: str) -> str:
    return dna.replace('T', 'U')


def test_dna_to_rna():
    assert dna_to_rna("TTTT") == "UUUU"
    assert dna_to_rna("GCAT") == "GCAU"
    assert dna_to_rna("GACCGCCGCC") == "GACCGCCGCC"
