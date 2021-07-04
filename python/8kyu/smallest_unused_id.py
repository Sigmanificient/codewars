def next_id(arr):
    """Kata url: https://www.codewars.com/kata/55eea63119278d571d00006a."""
    c = 0

    for item in sorted(set(arr)):
        if item != c:
            return c
        c += 1
    else:
        return c
