"""Kata url: https://www.codewars.com/kata/559f44187fa851efad000087."""


def seven_ate9(str_: str) -> str:
    while '797' in str_:
        str_ = str_.replace('797', '77')

    return str_


def test_seven_ate9():
    assert seven_ate9('797') == '77'
    assert seven_ate9('7979797') == '7777'
    assert seven_ate9('16797') == '1677'
    assert seven_ate9('77') == '77'
    assert seven_ate9('7927') == '7927'
    assert seven_ate9('1779') == '1779'
    assert seven_ate9('a779') == 'a779'
    assert seven_ate9('17797a') == '1777a'
    assert seven_ate9('797 9 7') == '77 9 7'
    assert seven_ate9('165561786121789797') == '16556178612178977'
