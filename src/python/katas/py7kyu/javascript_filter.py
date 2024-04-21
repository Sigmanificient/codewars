"""Kata url: https://www.codewars.com/kata/525d9b1a037b7a9da7000905."""


def search_names(logins):
    return list(filter(lambda x: x[0].endswith('_'), logins))


def test_search_names():
    foo_addr = "foo@foo.com"
    bar_addr = "bar@bar.com"

    a = [["foo", foo_addr], ["bar_", bar_addr]]
    b = [["bar_", bar_addr]]
    assert search_names(a) == b

    a = [["foobar_", foo_addr], ["bar_", bar_addr]]
    assert search_names(a) == b

    a = [["foo", foo_addr], ["bar", bar_addr]]
    assert search_names(a) == []

    import inspect

    assert "filter" in inspect.getsource(search_names)