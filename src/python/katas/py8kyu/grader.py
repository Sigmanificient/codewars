"""Kata url: https://www.codewars.com/kata/53d16bd82578b1fb5b00128c."""

from typing import Dict

GRADES: Dict[float, str] = {0.9: "A", 0.8: "B", 0.7: "C", 0.6: "D"}


def grader(grade: float) -> str:
    if grade > 1:
        return "F"

    return next((val for key, val in GRADES.items() if grade >= key), "F")


def test_grader():
    assert grader(0.6) == "D"
    assert grader(0.7) == "C"
    assert grader(0.8) == "B"
    assert grader(0.9) == "A"

    assert grader(0.1) == "F"
    assert grader(1.1) == "F"
    assert grader(0.0) == "F"
    assert grader(0.5) == "F"
