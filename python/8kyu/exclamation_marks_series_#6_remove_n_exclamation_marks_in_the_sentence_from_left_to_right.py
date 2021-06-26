def remove(s: str, n: int) -> str:
    """Kata url: https://www.codewars.com/kata/57faf7275c991027af000679."""
    r = []
    for char in s:
        if char == '!' and n:
            n -= 1
            continue

        r.append(char)
    return ''.join(r)
