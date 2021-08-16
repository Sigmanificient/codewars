import math


def find_next_square(sq: int) -> int:
    r: float = math.sqrt(sq)

    return -1 if r % 1 else (r + 1) ** 2
