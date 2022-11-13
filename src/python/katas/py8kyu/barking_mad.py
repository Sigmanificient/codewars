"""Kata url: https://www.codewars.com/kata/54dba07f03e88a4cec000caf."""


class Dog:
    def __init__(self, breed):
        self.breed = breed

    bark = staticmethod(lambda: "Woof")


snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")


def test_dg():
    assert snoopy.bark() == "Woof"
    assert scoobydoo.bark() == "Woof"
