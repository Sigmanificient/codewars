"""Kata url: https://www.codewars.com/kata/5571f712ddf00b54420000ee."""

CHANGES = {
    'Quarters': 25,
    'Dimes': 10,
    'Nickels': 5,
    'Pennies': 1
}


def loose_change(cents):
    if cents < 0:
        return {k: 0 for k in CHANGES.keys()}
    out = {}

    for k, v in CHANGES.items():
        got, cents = divmod(cents, v)
        out[k] = got

    return out


def test_loose_change():
    assert loose_change(29) == {
        'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {
        'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) == {
        'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {
        'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {
        'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
