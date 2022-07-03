from typing import List


def human_years_cat_years_dog_years(human_years: int) -> List[int]:
    c, d = 0, 0

    if human_years:
        d += 15

    if human_years > 1:
        d += 9

    c = d
    if human_years > 2:
        c += 4 * (human_years - 2)
        d += 5 * (human_years - 2)

    return [human_years, c, d]


def test_hy_cy_dy():
    assert human_years_cat_years_dog_years(1) == [1, 15, 15]
    assert human_years_cat_years_dog_years(2) == [2, 24, 24]
    assert human_years_cat_years_dog_years(10) == [10, 56, 64]
