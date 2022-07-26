"""Kata url: https://www.codewars.com/kata/52e88b39ffb6ac53a400022e."""


def int32_to_ip(int32: int) -> str:
    r, d = divmod(int32, 256)
    r, c = divmod(r, 256)
    a, b = divmod(r, 256)
    return f"{a}.{b}.{c}.{d}"


def test_int32_to_ip():
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(2149583361) == "128.32.10.1"
