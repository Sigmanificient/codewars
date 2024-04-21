"""Kata url: https://www.codewars.com/kata/52449b062fb80683ec000024."""

def generate_hashtag(s):
    if not s or len(s) > 140:
        return False

    return "#" + "".join(w.capitalize() for w in s.split(" ") if w)


def test_generate_hashtag():
    assert not generate_hashtag("")

    hash_out = generate_hashtag("Do We have A Hashtag")
    assert hash_out and hash_out[0] == "#"

    assert generate_hashtag("Codewars") == "#Codewars"
    assert generate_hashtag("Codewars      ") == "#Codewars"

    expected = "#CodewarsIsNice"
    assert generate_hashtag("Codewars Is Nice") == expected
    assert generate_hashtag("codewars is nice") == expected
    assert generate_hashtag("CodeWars is nice") == expected
    assert generate_hashtag("c i n") == "#CIN"
    assert generate_hashtag("codewars  is  nice") == expected
    assert not generate_hashtag(
        "Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
        "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
        "oooooooooooooooooooooooooooooooong Cat"
    )