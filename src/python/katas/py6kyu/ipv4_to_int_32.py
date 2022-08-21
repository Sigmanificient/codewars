"""Kata url: https://www.codewars.com/kata/52ea928a1ef5cfec800003ee."""


def ip_to_int32(ip: str) -> int:
    return int(''.join(f'{int(x):0>8b}' for x in ip.split('.')), 2)


def test_ip_to_int32():
    assert ip_to_int32("128.114.17.104") == 2154959208
    assert ip_to_int32("0.0.0.0") == 0
    assert ip_to_int32("128.32.10.1") == 2149583361
