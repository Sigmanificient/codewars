"""Kata url: https://www.codewars.com/kata/58dbdccee5ee8fa2f9000058."""


def sp_eng(sentence: str) -> bool:
    return "english" in sentence.lower()


def test_sp_eng():
    assert not sp_eng("")
    assert sp_eng("english")
    assert sp_eng("1234english ;k")
    assert sp_eng("English")
    assert sp_eng("eNgliSh")
    assert sp_eng("1234#$%%eNglish ;k9")
    assert not sp_eng("1234egn lis;h")
    assert not sp_eng("egnlish")
    assert not sp_eng("EGNlihs")
    assert not sp_eng("1234englihs**")
