"""Kara url: https://www.codewars.com/kata/51fda2d95d6efda45e00004e."""

class User:

    def __init__(self):
        self.rank = -8
        self.__progress = 0

    def inc_rank(self):
        self.rank += 1

        if self.rank == 0:
            self.rank += 1

        if self.rank > 8:
            self.rank = 8

    @property
    def progress(self):
        return self.__progress if self.rank != 8 else 0

    @staticmethod
    def check_progress(method):
        def wrapper(self, rank):
            method(self, rank)

            while self.__progress >= 100:
                self.__progress -= 100
                self.inc_rank()

            print(self.rank, self.__progress)

        return wrapper

    @check_progress
    def inc_progress(self, rank):
        if not rank or rank < -8 or rank > 8:
            raise ValueError

        if self.rank == 8:
            return

        if rank == self.rank:
            self.__progress += 3
            return

        z = (self.rank < 0 and rank > 0)
        if rank < self.rank:
            self.__progress += (self.rank - rank + z) < 3
            return

        d = rank - self.rank + z
        self.__progress += 10 * d * d


def test_user():
    user = User()

    assert user.rank == -8
    assert user.progress == 0

    user.inc_progress(-7)
    assert user.progress == 10

    user.inc_progress(-5)
    assert user.progress == 0
    assert user.rank == -7
