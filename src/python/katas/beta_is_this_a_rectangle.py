"""Kata url: https://www.codewars.com/kata/5e8bd9c9bc78a30033efe830."""

import math
from collections import namedtuple

Point = namedtuple('Point', ('x', 'y'))


def distance(a, b):
    return math.sqrt(
        (a.x - b.x) ** 2
        + (a.y - b.y) ** 2
    )


def is_this_a_rectangle(p, t=0.05):
    t = min(max(t, 0), 0.5)
    a, b, c, d, e = (Point(*k) for k in p)

    if len({a, b, c, d}) != 4:
        return False

    if (a != e) and distance(a, e) >= t:
        return False

    bd = distance(b, d)
    ac = distance(a, c)
    if ac == 0 or bd == 0:
        return False

    ab = distance(a, b)
    bc = distance(b, c)

    hyp = round(ac ** 2, 5)
    hyp_c = round((ab ** 2) + (bc ** 2), 5)

    if abs(hyp - hyp_c) > t:
        return False

    cd = distance(c, d)
    ad = distance(a, d)

    return (
        abs(ab - cd) <= t
        and abs(bc - ad) <= t
    )
