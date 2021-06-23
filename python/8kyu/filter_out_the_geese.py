from typing import List

geese: List[str] = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds: List[str]) -> List[str]:
    """Kata url: https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7."""
    return [bird for bird in birds if bird not in geese]
