"""Kata url: https://www.codewars.com/kata/57fb44a12b53146fe1000136."""


def weight(k):
    return sum({'!': 3, '?': 2}.get(c, 0) for c in k)


def balance(left, right):
    x = weight(left) - weight(right)
    if x == 0:
        return "Balance"
    return "left" if x < 0 else "right"


def test_balance():
    assert balance("", "") == "Balance"
    assert balance("!!", "??") == "Right"
    assert balance("!??", "?!!") == "Left"
    assert balance("!?!!", "?!?") == "Left"
    assert balance("!!???!????", "??!!?!!!!!!!") == "Balance"
