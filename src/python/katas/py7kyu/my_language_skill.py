"""Kata url: https://www.codewars.com/kata/5b16490986b6d336c900007d."""


def my_languages(results):
    return [
        lang for lang, score in sorted(
            results.items(),
            key=lambda x: x[1],
            reverse=True
        ) if score >= 60
    ]


def test_my_languages():
    assert my_languages(
        {"Java": 10, "Ruby": 80, "Python": 65}
    ) == ["Ruby", "Python"]
    assert my_languages(
        {"Hindi": 60, "Greek": 71, "Dutch": 93}
    ) == ["Dutch", "Greek", "Hindi"]
    assert my_languages({"C++": 50, "ASM": 10, "Haskell": 20}) == []
