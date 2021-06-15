def abbrev_name(name: str) -> str:
    """Kata url: https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3."""
    return '.'.join(word[0].upper() for word in name.split())
