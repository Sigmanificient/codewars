def find_nb(m: int) -> int:
    vol, n = 0, 2

    while vol < m:
        vol += (n - 1) ** 3
        n += 1

    return (n - 2) if m == vol else -1


def test_find_nb():
    assert find_nb(24723578342962) == -1
    assert find_nb(4183059834009) == 2022
    assert find_nb(135440716410000) == 4824
    assert find_nb(40539911473216) == 3568
    assert find_nb(26825883955641) == 3218
