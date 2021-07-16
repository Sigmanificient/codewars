from typing import List


def anagrams(word: str, words: List[str]) -> List[str]:
    """Kata url: https://www.codewars.com/kata/523a86aa4230ebb5420001e1."""
    sorted_word: List[str] = sorted(word)
    return [wrd for wrd in words if sorted(wrd) == sorted_word]
