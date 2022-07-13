"""Kata url: https://www.codewars.com/kata/56f6919a6b88de18ff000b36."""

def how_many_dalmatians(n: int) -> str:
    dogs = [
        "Hardly any", "More than a handful!",
        "Woah that's a lot of dogs!", "101 DALMATIONS!!!"
    ]

    if n <= 10:
        return dogs[0]
    elif n <= 50:
        return dogs[1]
    elif n == 101:
        return dogs[3]
    else:
        return dogs[2]


def test_how_many_dalmatians():
    assert how_many_dalmatians(26) == "More than a handful!"
    assert how_many_dalmatians(8) == "Hardly any"
    assert how_many_dalmatians(14) == "More than a handful!"
    assert how_many_dalmatians(80) == "Woah that's a lot of dogs!"
    assert how_many_dalmatians(100) == "Woah that's a lot of dogs!"
    assert how_many_dalmatians(50) == "More than a handful!"
    assert how_many_dalmatians(10) == "Hardly any"
    assert how_many_dalmatians(101) == "101 DALMATIONS!!!"
