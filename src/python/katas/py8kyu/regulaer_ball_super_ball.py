"""Kata url: https://www.codewars.com/kata/53f0f358b9cb376eca001079."""


class Ball:

    def __init__(self, _type="regular"):
        self.ball_type = _type


def test_ball():
    assert Ball().ball_type == "regular"
    assert Ball('super').ball_type == "super"
