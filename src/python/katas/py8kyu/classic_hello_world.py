"""Kata url: https://www.codewars.com/kata/57036f007fd72e3b77000023."""


class Solution:

    @staticmethod
    def main(*_args):
        print("Hello World!")


def test_solution():
    assert Solution.main() == "Hello World!"
    assert Solution.main("Hola mundo!") == "Hello World!"
