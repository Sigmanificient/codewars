import math
from typing import List, Optional


def is_prime(k: int) -> bool:
    return k == 2 or (
            k > 2 and k % 2
            and all(k % i for i in range(3, int(math.sqrt(k)) + 1, 2))
    )


def gap(g: int, m: int, n: int) -> Optional[List[int]]:
    _lp = -1

    for i in range(m, n + 1):
        if not is_prime(i):
            continue

        if i - _lp == g:
            return [_lp, i]

        _lp = i

    return None


def test_gap():
    assert gap(6, 100, 110) is None
    assert gap(2, 100, 110) == [101, 103]
    assert gap(4, 100, 110) == [103, 107]
    assert gap(8, 300, 400) == [359, 367]
    assert gap(10, 300, 400) == [337, 347]
    assert gap(2, 100, 103) == [101, 103]
