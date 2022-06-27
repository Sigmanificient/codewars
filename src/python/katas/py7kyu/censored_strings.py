def uncensor(infected: str, discovered: str) -> str:
    for i in discovered:
        infected = infected.replace('*', i, 1)

    return infected


def test_uncensor():
    assert uncensor('', '') == ''
    assert uncensor('', 'abc') == ''
    assert uncensor('abc', '') == 'abc'

    assert uncensor('***', 'abc') == 'abc'
    assert uncensor('A**Z*N*', 'MAIG') == 'AMAZING'
    assert uncensor('*h*s *s v*ry *tr*ng*', 'Tiiesae') == 'This is very strange'


