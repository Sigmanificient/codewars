"""Kata url: https://www.codewars.com/kata/5676ffaa8da527f234000025."""
from itertools import permutations


def sc_perm_comb(num: int) -> int:
    str_num = str(num)
    n_len = len(str_num)

    return sum(
        {
            int(''.join(p))
            for i in range(1, n_len + 1)
            for p in set(permutations(str_num, i))
        }
    )


def test_sc_perm_comb():
    assert sc_perm_comb(348) == 3675
    assert sc_perm_comb(340) == 1631
    assert sc_perm_comb(333) == 369
    assert sc_perm_comb(6) == 6
    assert sc_perm_comb(0) == 0
