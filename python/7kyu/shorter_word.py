def find_short(s: str) -> int:
    """Kata url: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9."""
    return len(sorted(s.split(), key=len)[0])
