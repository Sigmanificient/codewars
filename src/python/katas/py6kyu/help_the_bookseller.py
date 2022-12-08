"""Kata url: https://www.codewars.com/kata/54dc6f5a224c26032800005c."""


def stock_list(list_of_art, list_of_cat):
    if not list_of_cat or not list_of_art:
        return ''

    data = {k: 0 for k in list_of_cat}

    for art in list_of_art:
        k = art[0]
        if k in data:
            data[k] += int(art.split()[1])

    return " - ".join(f"({k} : {v})" for k, v in data.items())


def test_stock_list():
    assert stock_list(
        ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"],
        ["A", "B", "C", "D"]
    ) == "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"

    assert stock_list(
        ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"],
        ["A", "B"]
    ) == "(A : 200) - (B : 1140)"
