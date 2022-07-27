def same_case(a, b):
    return (-1 + (a+b).isalpha()) or (a.isupper() == b.isupper())


def test_same_case():
    assert same_case('C', 'B') == 1
    assert same_case('b', 'a') == 1
    assert same_case('d', 'd') == 1
    assert same_case('A', 's') == 0
    assert same_case('c', 'B') == 0
    assert same_case('b', 'Z') == 0
    assert same_case('\t', 'Z') == -1
    assert same_case('H', ':') == -1
