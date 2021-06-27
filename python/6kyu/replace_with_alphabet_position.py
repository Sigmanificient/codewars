alphabet: str = "abcdefghijklmnopqrstuvwxyz"


def alphabet_position(text: str) -> str:
    """Kata url: https://www.codewars.com/kata/546f922b54af40e1e90001da."""
    return ' '.join(str(alphabet.index(char) + 1) for char in text.lower() if char in alphabet)
