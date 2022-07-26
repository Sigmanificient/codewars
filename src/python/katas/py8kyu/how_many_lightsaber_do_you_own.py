"""Kata url: https://www.codewars.com/kata/51f9d93b4095e0a7200001b8."""


def how_many_light_sabers_do_you_own(name: str = "") -> int:
    return 0 if name != "Zach" else 18


def test_how_many_light_sabers():
    assert how_many_light_sabers_do_you_own("Zach") == 18
    assert how_many_light_sabers_do_you_own() == 0
    assert how_many_light_sabers_do_you_own("zach") == 0
