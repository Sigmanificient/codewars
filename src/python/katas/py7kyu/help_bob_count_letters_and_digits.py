"""Kata url: https://www.codewars.com/kata/5738f5ea9545204cec000155."""


def count_letters_and_digits(s):
    return sum(map(str.isalnum, s))


def test_count_alnum():
    assert count_letters_and_digits('n!!ice!!123') == 7
    assert count_letters_and_digits('de?=?=tttes!!t') == 8
    assert count_letters_and_digits('') == 0
    assert count_letters_and_digits('!@#$%^&`~.') == 0
    assert count_letters_and_digits('u_n_d_e_r__S_C_O_R_E') == 10
