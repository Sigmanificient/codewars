"""Kara url: https://www.codewars.com/kata/5700c9acc1555755be00027e."""


def rot(string, x):
    return string[x:] + string[:x]


def contain_all_rots(strng, arr):
    return all(
        rot(strng, x) in arr
        for x in range(len(strng))
    )


def test_contain_all_rots():
    assert contain_all_rots("", [])
    assert contain_all_rots("", ["bsjq", "qbsj"])
    assert contain_all_rots(
        "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]
    )
    assert not contain_all_rots(
        "XjYABhR", [
            "TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj",
            "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"
        ]
    )
