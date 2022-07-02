def show_sequence(n: int) -> int:
    if not n:
        return '0=0'

    if n < 0:
        return f'{n}<0'

    r = range(n + 1)
    return f"{'+'.join(map(str, r))} = {sum(r)}"


def test_show_sequence():
    assert show_sequence(6) == "0+1+2+3+4+5+6 = 21"
    assert show_sequence(7) == "0+1+2+3+4+5+6+7 = 28"
    assert show_sequence(0) == "0=0"
    assert show_sequence(-1) == "-1<0"
    assert show_sequence(-10) == "-10<0"
