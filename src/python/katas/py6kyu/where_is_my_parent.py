"""kata url: https://www.codewars.com/kata/58539230879867a8cd00011c."""


def find_children(dancing_brigade):
    return ''.join(
        sorted(
            dancing_brigade,
            key=lambda x: ord(x.lower()) * 2 + x.islower()
        )
    )


def test_find_children():
    assert find_children("abBA") == "AaBb"
    assert find_children("AaaaaZazzz") == "AaaaaaZzzz"
    assert find_children("CbcBcbaA") == "AaBbbCcc"
    assert find_children("xXfuUuuF") == "FfUuuuXx"
    assert find_children("") == ""
