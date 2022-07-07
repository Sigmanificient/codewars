"""Kata url: https://www.codewars.com/kata/5672a98bdbdd995fad00000f."""


def rps(p1, p2):
    if p1 == p2:
        return "Draw!"

    win = {
        'paper': 'scissors',
        'scissors': 'rock',
        'rock': 'paper'
    }[p1]
    return f"Player {1 + (win == p2)} won!"


def test_rps():
    assert rps('rock', 'scissors') == "Player 1 won!"
    assert rps('scissors', 'rock') == "Player 2 won!"
    assert rps('rock', 'rock') == 'Draw!'
