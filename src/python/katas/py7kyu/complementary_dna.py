def dna_strand(dna: str) -> str:
    return dna.translate(dna.maketrans('ACGT', 'TGCA'))
