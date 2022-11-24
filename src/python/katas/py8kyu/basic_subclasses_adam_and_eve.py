"""Kata url: https://www.codewars.com/kata/547274e24481cfc469000416."""
Human = type('Human', (), {})
Man = type('Man', (Human,), {})
Woman = type('Woman', (Human,), {})


def god():
    return [Man(), Woman()]


def test_got():
    h = god()
    assert isinstance(h[0], Man)
    assert isinstance(h[1], Woman)
    assert isinstance(h[0], Human)
    assert isinstance(h[1], Human)
