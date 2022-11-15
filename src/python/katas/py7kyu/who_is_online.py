"""Kata url: https://www.codewars.com/kata/5b6375f707a2664ada00002a."""
from collections import defaultdict


def who_is_online(friends):
    out = defaultdict(list)

    for f in friends:
        user = f["username"]
        if f["status"] == "offline":
            out["offline"].append(user)
            continue

        status = "online" if f["last_activity"] <= 10 else "away"
        out[status].append(user)
    return out


def test_who_is_online():
    assert who_is_online([
        {"username": "David", "status": "online", "last_activity": 10},
        {"username": "Lucy", "status": "offline", "last_activity": 22},
        {"username": "Bob", "status": "online", "last_activity": 104}
    ]) == {"online": ["David"], "offline": ["Lucy"], "away": ["Bob"]}

    assert who_is_online([
        {"username": "Lucy", "status": "offline", "last_activity": 22},
        {"username": "Bob", "status": "online", "last_activity": 104}
    ]) == {"offline": ["Lucy"], "away": ["Bob"]}
