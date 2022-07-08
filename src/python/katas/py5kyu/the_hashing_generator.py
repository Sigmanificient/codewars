"""Kata url: https://www.codewars.com/kata/52449b062fb80683ec000024."""

from typing import Optional


def generate_hashtag(s) -> Optional[str]:
    if not s or len(s) > 140:
        return False

    return '#' + ''.join(
        w.capitalize() for w in s.split(' ') if w
    )


def test_generate_hashtag():
    assert not generate_hashtag('')
    assert generate_hashtag('Do We have A Hashtag')[0] == '#'
    assert generate_hashtag('Codewars') == '#Codewars'
    assert generate_hashtag('Codewars      ') == '#Codewars'
    assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'
    assert generate_hashtag('codewars is nice') == '#CodewarsIsNice'
    assert generate_hashtag('CodeWars is nice') == '#CodewarsIsNice'
    assert generate_hashtag('c i n') == '#CIN'
    assert generate_hashtag('codewars  is  nice') == '#CodewarsIsNice'
    assert not generate_hashtag(
        'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'
        'oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'
        'oooooooooooooooooooooooooooooooong Cat'
    )