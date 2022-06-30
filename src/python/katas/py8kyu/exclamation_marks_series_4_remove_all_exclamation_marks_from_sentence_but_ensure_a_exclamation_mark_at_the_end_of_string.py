# Kata url: https://www.codewars.com/kata/57faf12b21c84b5ba30001b0.

def remove(s: str) -> str:
    return s.replace('!', '') + '!'


def test_move():
    assert remove("Hi!") == "Hi!"
    assert remove("Hi!!!") == "Hi!"
    assert remove("!Hi") == "Hi!"
    assert remove("!Hi!") == "Hi!"
    assert remove("Hi! Hi!") == "Hi Hi!"
    assert remove("Hi") == "Hi!"
