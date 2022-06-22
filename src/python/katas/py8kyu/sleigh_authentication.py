"""Kata url: https://www.codewars.com/kata/52adc142b2651f25a8000643."""


class Sleigh:

    @staticmethod
    def authenticate(name, password):
        return name == "Santa Claus" and password == "Ho Ho Ho!"


def test_sleigh():
    sleigh = Sleigh()

    assert sleigh.authenticate('Santa Claus', 'Ho Ho Ho!')
    assert not sleigh.authenticate('Santa', 'Ho Ho Ho!')
    assert not sleigh.authenticate('Santa Claus', 'Ho Ho!')
    assert not sleigh.authenticate('jhoffner', 'CodeWars')
