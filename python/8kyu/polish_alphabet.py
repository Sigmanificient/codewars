transcriptions = {
    "ą": "a",
    "ć": "c",
    "ę": "e",
    "ł": "l",
    "ń": "n",
    "ó": "o",
    "ś": "s",
    "ź": "z",
    "ż": "z"
}


def correct_polish_letters(st: str) -> str:
    """Kata url: https://www.codewars.com/kata/57ab2d6072292dbf7c000039."""
    return ''.join(transcriptions.get(char, char) for char in st)
