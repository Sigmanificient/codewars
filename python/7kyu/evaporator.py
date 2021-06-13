def evaporator(content: int, evap_per_day: int, threshold: int) -> int:
    """Kata url: https://www.codewars.com/kata/5506b230a11c0aeab3000c1f."""
    c = 0
    mn = content * (threshold / 100)

    while content > mn:
        content *= 1 - (evap_per_day / 100)
        c += 1
    return c
