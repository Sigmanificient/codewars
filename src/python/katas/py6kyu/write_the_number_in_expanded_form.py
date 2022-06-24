def expanded_form(num):
    return ' + '.join(
        f"{i:0{(len(str(num)) - c)}}"
        for c, i in enumerate(str(num))
        if i != '0'
    )


def test_expanded_form():
    assert expanded_form(12) == '10 + 2'
    assert expanded_form(42) == '40 + 2'
    assert expanded_form(70304) == '70000 + 300 + 4'
