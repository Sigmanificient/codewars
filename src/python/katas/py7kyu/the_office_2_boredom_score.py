"""Kata url: https://www.codewars.com/kata/57ed4cef7b45ef8774000014."""

SCORES = {
    "accounts": 1,
    "finance": 2,
    "canteen": 10,
    "regulation": 3,
    "trading": 6,
    "change": 6,
    "IS": 8,
    "retail": 5,
    "cleaning": 4,
    "pissing about": 25
}


def boredom(staff):
    total = sum(SCORES[i] for i in staff.values())
    if total > 100:
        return 'party time!!'
    if total < 80:
        return 'kill me now'
    return 'i can handle this'
