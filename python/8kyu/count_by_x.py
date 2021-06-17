from typing import List


def count_by(x: int, n: int) -> List[int]:
    return list(range(x, x * n + 1, x))
