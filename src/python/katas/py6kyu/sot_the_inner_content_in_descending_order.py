"""Kata url: https://www.codewars.com/kata/5898b4b71d298e51b600014b."""


def sort_the_inner_content(words):
    out = []

    for word in words.split(' '):
        if len(word) < 3:
            out.append(word)
            continue

        first, *content, last = word

        out.append(
            first
            + ''.join(sorted(content, reverse=True))
            + last
        )

    return ' '.join(out)


def test_sort_the_inner_content():
    assert sort_the_inner_content(
        "sort the inner content in descending order"
    ) == "srot the inner ctonnet in dsnnieedcg oredr"

    assert sort_the_inner_content("wait for me") == "wiat for me"
    assert sort_the_inner_content("this kata is easy") == "tihs ktaa is esay"
