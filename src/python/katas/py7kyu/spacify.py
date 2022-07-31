"""Kata url: https://www.codewars.com/kata/62dcbe87f4ac96005f052962."""


def spacify(string: str) -> str:
    return " ".join(string)


def test_spacify():
    assert spacify("") == ""
    assert spacify("a") == "a"

    assert spacify("hello world") == "h e l l o   w o r l d"
    assert spacify("12345") == "1 2 3 4 5"
    assert spacify("Pippi") == "P i p p i"
