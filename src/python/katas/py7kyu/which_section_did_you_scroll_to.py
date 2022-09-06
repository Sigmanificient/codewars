"""Kata url: https://www.codewars.com/kata/5cb05eee03c3ff002153d4ef."""


def get_section_id(scroll, sizes):
    for c, s in enumerate(sizes):
        scroll -= s

        if scroll < 0:
            return c

    return -1


def test_get_section_id():
    assert get_section_id(1, [300, 200, 400, 600, 100]) == 0
    assert get_section_id(299, [300, 200, 400, 600, 100]) == 0
    assert get_section_id(300, [300, 200, 400, 600, 100]) == 1
    assert get_section_id(1599, [300, 200, 400, 600, 100]) == 4
    assert get_section_id(1600, [300, 200, 400, 600, 100]) == -1
