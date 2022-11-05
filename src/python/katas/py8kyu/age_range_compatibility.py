"""Kata url: https://www.codewars.com/kata/5803956ddb07c5c74200144e."""

def dating_range(age):
    if age <= 14:
        return f"{int(age - .1 * age)}-{int(age + .1 * age)}"

    return f"{int(age / 2 + 7)}-{(age - 7) * 2}"


def test_dating_rage():
    assert dating_range(17) == "15-20"
    assert dating_range(40) == "27-66"
    assert dating_range(15) == "14-16"
    assert dating_range(35) == "24-56"
    assert dating_range(10) == "9-11"
