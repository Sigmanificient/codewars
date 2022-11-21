"""Kata url: https://www.codewars.com/kata/55327e12f5363713200000e4."""


def is_jojo(name):
    first, *_, last = name.lower().split(' ')

    return (
        (first.startswith('jo') and last.startswith('jo'))
        or (first.startswith('jo') and last.endswith('jo'))
        or (first.startswith('gio') and last.startswith('gio'))
    )


def test_is_jojo():
    assert is_jojo("Jonathan Joestar")
    assert not is_jojo("Dio Brando")
    assert not is_jojo("Joseph Giovanna")
    assert not is_jojo("Giorno Joestar")
    assert not is_jojo("Joe Giorgio")
    assert not is_jojo("Giorno Baggio")
