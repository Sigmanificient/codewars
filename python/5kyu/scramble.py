def scramble(s1: str, s2: str) -> bool:
    """Kata url: https://www.codewars.com/kata/55c04b4cc56a697bb0000048."""
    return all(s1.count(x) >= s2.count(x) for x in sorted(set(s2)))
