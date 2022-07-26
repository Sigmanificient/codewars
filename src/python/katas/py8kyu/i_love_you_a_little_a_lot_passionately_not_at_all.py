"""Kata url: https://www.codewars.com/kata/57f24e6a18e9fad8eb000296."""


def how_much_i_love_you(nb_petals: int) -> str:
    return ("I love you", "a little", "a lot", "passionately", "madly", "not at all")[
        (nb_petals - 1) % 6
    ]


def test_how_much_i_love_you():
    assert how_much_i_love_you(1) == "I love you"
    assert how_much_i_love_you(2) == "a little"
    assert how_much_i_love_you(3) == "a lot"
    assert how_much_i_love_you(4) == "passionately"
    assert how_much_i_love_you(5) == "madly"
    assert how_much_i_love_you(6) == "not at all"
    assert how_much_i_love_you(7) == "I love you"

    assert how_much_i_love_you(500) == "a little"

    assert how_much_i_love_you(501) == "a lot"
    assert how_much_i_love_you(9999) == "a lot"
