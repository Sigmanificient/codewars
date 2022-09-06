"""Kata url: https://www.codewars.com/kata/5962bbea6878a381ed000036."""


class HighScoreTable:

    def __init__(self, limit):
        self.scores = []
        self.limit = limit

    def update(self, score):
        self.scores = sorted(self.scores + [score], reverse=True)[:self.limit]

    def reset(self):
        self.scores.clear()


def test_high_score_table():
    hst = HighScoreTable(3)
    assert hst.scores == []

    hst.update(10)
    assert hst.scores == [10]

    hst.update(8)
    hst.update(12)
    assert hst.scores == [12, 10, 8]

    hst.update(5)
    assert hst.scores == [12, 10, 8]

    hst.update(10)
    assert hst.scores == [12, 10, 10]

    hst.update(10)
    assert hst.scores == [12, 10, 10]

    hst.update(20)
    assert hst.scores == [20, 12, 10]

    hst.update(20)
    assert hst.scores == [20, 20, 12]

    hst.update(20)
    assert hst.scores == [20, 20, 20]

    hst.reset()
    assert hst.scores == []
