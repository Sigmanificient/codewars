"""Kata url: https://www.codewars.com/kata/57036f007fd72e3b77000023."""


class Solution:

    @staticmethod
    def main(*_args):
        print("Hello World!")


def test_solution():
    import io
    from contextlib import redirect_stdout

    def _test_stdout(func, *args):
        with io.StringIO() as buf, redirect_stdout(buf):
            func(*args)
            return buf.getvalue().strip()

    assert _test_stdout(Solution.main) == "Hello World!"
    assert _test_stdout(Solution.main, "Hi!") == "Hello World!"
