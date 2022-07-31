"""Kata url: https://www.codewars.com/kata/5263c6999e0f40dee200059d."""


def get_pins(observed):
    each_comb = []
    layout = "123456789 0 "

    for o_digit in observed:
        i = layout.index(o_digit)
        pos = [i - 3, i - 1, i + 1, i + 3]
        neighbours = []

        for c, p in enumerate(pos):
            if p > len(layout) or p < 0:
                continue

            v = layout[p]
            if v == " ":
                continue

            if c == 1 and not int(v) % 3:
                continue

            if c == 2 and int(v) % 3 == 1:
                continue

            neighbours.append(v)

        each_comb.append(neighbours + [o_digit])

    out = []
    comb_length = [len(l) for l in each_comb]

    total_comb = 1
    for x in comb_length:
        total_comb *= x

    for i in range(total_comb):
        comb = ""
        for j in range(len(comb_length)):
            comb += each_comb[j][i % comb_length[j]]
            i //= comb_length[j]
        out.append(comb)
    return out


def test_get_pins():
    assert sorted(get_pins("8")) == sorted(["5", "7", "8", "9", "0"])
    assert sorted(get_pins("11")) == sorted(
        ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
    )

    assert sorted(get_pins("369")) == sorted(
        [
            "339",
            "366",
            "399",
            "658",
            "636",
            "258",
            "268",
            "669",
            "668",
            "266",
            "369",
            "398",
            "256",
            "296",
            "259",
            "368",
            "638",
            "396",
            "238",
            "356",
            "659",
            "639",
            "666",
            "359",
            "336",
            "299",
            "338",
            "696",
            "269",
            "358",
            "656",
            "698",
            "699",
            "298",
            "236",
            "239",
        ]
    )

    assert sorted(get_pins("147")) == sorted(
        [
            "114",
            "117",
            "118",
            "144",
            "147",
            "148",
            "154",
            "157",
            "158",
            "174",
            "177",
            "178",
            "214",
            "217",
            "218",
            "244",
            "247",
            "248",
            "254",
            "257",
            "258",
            "274",
            "277",
            "278",
            "414",
            "417",
            "418",
            "444",
            "447",
            "448",
            "454",
            "457",
            "458",
            "474",
            "477",
            "478",
        ]
    )
