def evaporator(content: int, evap_per_day: int, threshold: int) -> int:
    c = 0
    mn = content * (threshold / 100)

    while content > mn:
        content *= 1 - (evap_per_day / 100)
        c += 1
    return c
