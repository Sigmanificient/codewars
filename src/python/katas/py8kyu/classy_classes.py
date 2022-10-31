"""Kata url: https://www.codewars.com/kata/55a144eff5124e546400005a."""

class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


def test_person():
    person = Person("John", 30)
    assert person.info == "Johns age is 30"
