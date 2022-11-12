"""Kara url: https://www.codewars.com/kata/529b418d533b76924600085d."""


def to_underscore(string):
    if not isinstance(string, str):
        return str(string)

    out = ""
    for i, c in enumerate(string):
        if i and c.isupper():
            out += '_'

        out += c.lower()
    return out


def test_to_underscore():
    assert to_underscore('TestController') == 'test_controller'
    assert to_underscore('ThisIsBeautifulDay') == 'this_is_beautiful_day'
    assert to_underscore('Am7Days') == 'am7_days'
    assert to_underscore('My3CodeIs4TimesBetter') == 'my3_code_is4_times_better'
    assert to_underscore(5) == '5'
