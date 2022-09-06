"""Kata url: https://www.codewars.com/kata/56f3a1e899b386da78000732."""


def partlist(arr):
    return [
        (' '.join(arr[:i]), ' '.join(arr[i:]))
        for i in range(1, len(arr))
    ]


def test_partlist():
    assert partlist(["I", "wish", "I", "hadn't", "come"]) == [
        ("I", "wish I hadn't come"),
        ("I wish", "I hadn't come"),
        ("I wish I", "hadn't come"),
        ("I wish I hadn't", "come")
    ]

    assert partlist(["cdIw", "tzIy", "xDu", "rThG"]) == [
        ("cdIw", "tzIy xDu rThG"),
        ("cdIw tzIy", "xDu rThG"),
        ("cdIw tzIy xDu", "rThG")
    ]

    assert partlist(["vJQ", "anj", "mQDq", "sOZ"]) == [
        ("vJQ", "anj mQDq sOZ"),
        ("vJQ anj", "mQDq sOZ"),
        ("vJQ anj mQDq", "sOZ")
    ]

    assert partlist(["mkC", "WoiP", "pCHh", "mkv"]) == [
        ("mkC", "WoiP pCHh mkv"),
        ("mkC WoiP", "pCHh mkv"),
        ("mkC WoiP pCHh", "mkv")
    ]

    assert partlist(["vHW", "bPq", "pme", "jJr", "HGHV"]) == [
        ("vHW", "bPq pme jJr HGHV"),
        ("vHW bPq", "pme jJr HGHV"),
        ("vHW bPq pme", "jJr HGHV"),
        ("vHW bPq pme jJr", "HGHV")
    ]

    assert partlist(["YZd", "ptUD", "IXr"]) == [
        ("YZd", "ptUD IXr"), ("YZd ptUD", "IXr")
    ]
