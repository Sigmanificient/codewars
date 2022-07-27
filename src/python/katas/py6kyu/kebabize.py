def kebabize(string: str) -> str:
    return ''.join(
        f"{'-' * (c != 0)}{char.lower()}" if char.isupper() else char
        for c, char in enumerate(filter(str.isalpha, string))
    )


def test_kebabize():
    assert kebabize('myCamelCasedString') == 'my-camel-cased-string'
    assert kebabize('myCamelHas3Humps') == 'my-camel-has-humps'
    assert kebabize('SOS') == 's-o-s'
    assert kebabize('42') == ''
    assert kebabize('CodeWars') == 'code-wars'
