"""Kata url: https://www.codewars.com/kata/525d9b1a037b7a9da7000905."""


def search_names(logins):
    return list(filter(lambda x: x[0].endswith('_'), logins))


def test_search_names():
    a = [["foo", "foo@foo.com"], ["bar_", "bar@bar.com"]]
    b = [["bar_", "bar@bar.com"]]
    assert search_names(a) == b

    a = [["foobar_", "foo@foo.com"], ["bar_", "bar@bar.com"]]
    b = [["foobar_", "foo@foo.com"], ["bar_", "bar@bar.com"]]
    assert search_names(a) == b

    a = [["foo", "foo@foo.com"], ["bar", "bar@bar.com"]]
    b = []
    assert search_names(a) == b

    import inspect

    assert "filter" in inspect.getsource(search_names)
