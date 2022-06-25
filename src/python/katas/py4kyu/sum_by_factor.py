from collections import defaultdict
from math import sqrt


def get_abs_prime_factors(n):
    if n < 0:
        n = -n

    result = set()
    for i in range(2, int(sqrt(n)) + 1):
        while not n % i:
            result.add(i)
            n //= i

    if n > 1:
        result.add(n)

    return result


def sum_for_list(lst):
    p = defaultdict(list)

    for item in lst:
        for f in get_abs_prime_factors(item):
            p[f].append(item)

    return [[k, sum(p[k])] for k in sorted(p.keys())]


def test_abs_prime_factors():
    assert get_abs_prime_factors(25) == {5}
    assert get_abs_prime_factors(7 * 5) == {5, 7}
    assert get_abs_prime_factors(100) == {2, 5}
    assert get_abs_prime_factors(3301) == {3301}
    assert get_abs_prime_factors(7775460) == {2, 3, 5, 7, 11, 17}
    assert get_abs_prime_factors(-7775460) == {2, 3, 5, 7, 11, 17}


def test_sum_for_list():
    assert sum_for_list([12, 15]) == [[2, 12], [3, 27], [5, 15]]
    assert sum_for_list(
        [15, 21, 24, 30, 45]
    ) == [[2, 54], [3, 135], [5, 90], [7, 21]]
