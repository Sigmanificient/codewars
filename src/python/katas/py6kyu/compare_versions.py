"""Kata url: https://www.codewars.com/kata/53b138b3b987275b46000115."""


def compare_versions(v1, v2):
    v1s = v1.split('.')
    v2s = v2.split('.')

    l1 = len(v1s)
    l2 = len(v2s)

    if l1 > l2:
        v2s.extend(['0'] * (l1 - l2))
    elif l2 > l1:
        v1s.extend(['0'] * (l2 - l1))

    return all(int(x) >= int(y) for x, y in zip(v1s, v2s))


def test_compare_versions():
    assert compare_versions("11", "10")
    assert compare_versions("11", "11")

    assert compare_versions("10.4.6", "10.4")
    assert not compare_versions("10.4", "10.4.8")
    assert compare_versions("10.4", "11")
    assert compare_versions("10.4", "10.10")
    assert compare_versions("10.4.9", "10.5")
