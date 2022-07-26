"""Kata url: https://www.codewars.com/kata/526989a41034285187000de4."""


def ips_between(start: str, end: str) -> int:
    grs_end = [int(n) for n in end.split(".")]
    grs_start = [int(n) for n in start.split(".")]

    return sum(
        (g_e - g_s) * (256 ** (3 - p))
        for p, (g_s, g_e) in enumerate(zip(grs_start, grs_end))
    )


def test_ips_between():
    assert ips_between("10.0.0.0", "10.0.0.50") == 50
    assert ips_between("10.0.0.0", "10.0.1.0") == 256
    assert ips_between("20.0.0.10", "20.0.1.0") == 246
    assert ips_between("0.0.0.0", "255.255.255.255") == 4294967295
