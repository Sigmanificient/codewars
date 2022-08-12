"""Kata url: https://www.codewars.com/kata/57280481e8118511f7000ffa."""


def split_and_merge(string_: str, sep: str) -> str:
    return ' '.join(
        sep.join(word)
        for word in string_.split(' ')
    )


def test_split_and_merge():
    assert split_and_merge("My name is John", " ") == "M y n a m e i s J o h n"
    assert split_and_merge("My name is John", "-") == "M-y n-a-m-e i-s J-o-h-n"
    assert split_and_merge("Hello World!", ".") == "H.e.l.l.o W.o.r.l.d.!"
    assert split_and_merge("Hello World!", ",") == "H,e,l,l,o W,o,r,l,d,!"
