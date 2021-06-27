def nb_year(p0: int, percent: float, aug: int, final: int) -> int:
    """Kata url: https://www.codewars.com/kata/563b662a59afc2b5120000c6."""
    y: int = 0
    m: int = p0
    percent /= 100

    while m < final:
        m = int(m + (m * percent) + aug)
        y += 1
    return y
