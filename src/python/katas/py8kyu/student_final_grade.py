"""Kata url: https://www.codewars.com/kata/5ad0d8356165e63c140014d4."""


def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100

    if exam > 75 and projects >= 5:
        return 90

    if exam > 50 and projects >= 2:
        return 75

    return 0


def test_final_grade():
    assert final_grade(100, 12) == 100
    assert final_grade(99, 0) == 100
    assert final_grade(10, 15) == 100
    assert final_grade(85, 5) == 90
    assert final_grade(55, 3) == 75
    assert final_grade(55, 0) == 0
    assert final_grade(20, 2) == 0
