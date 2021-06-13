def get_middle(s: str) -> str:
    length: int = len(s)
    middle: int = length // 2
    return s[middle - (not length % 2):middle + 1]
