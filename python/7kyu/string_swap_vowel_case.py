# Kata url: https://www.codewars.com/kata/5803c0c6ab6c20a06f000026.

def swap_vowel_case(st: str) -> str:
    return ''.join(
        x.swapcase() if x.lower() in 'aeoui' else x for x in st
    )
