"""Kata url: https://www.codewars.com/kata/57f21fcd69e09cb0d2000088."""

import re


def rearrange(addr: str) -> str:
    matched = re.match(r"(http:\/{2}[A-z.-]*)[.]([^\/]+)\/?(.*)", addr)
    assert matched is not None
    prefix, dom, suffix = matched.groups()

    return (
        { 'com': 'a', 'gov': 'b', 'org': 'c' }.get(dom, 'z')
        + dom + prefix + suffix
    )


def order_by_domain(addresses):
    return sorted(addresses, key=rearrange)