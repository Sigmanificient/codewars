"""Kata url: https://www.codewars.com/kata/5827acd5f524dd029d0005a4."""


def is_ruby_coming(lst):
    return any(
        p['language'] == 'Ruby'
        for p in lst
    )


def test_is_ruby_coming():
    assert is_ruby_coming(
        [
            {
                'firstName': 'Sofia',
                'lastName': 'I.',
                'country': 'Argentina',
                'continent': 'Americas',
                'age': 35,
                'language': 'Java'
            },
            {
                'firstName': 'Lukas',
                'lastName': 'X.',
                'country': 'Croatia',
                'continent': 'Europe',
                'age': 35,
                'language': 'Python'
            },
            {
                'firstName': 'Madison',
                'lastName': 'U.',
                'country': 'United States',
                'continent': 'Americas',
                'age': 32,
                'language': 'Ruby'
            }
        ]
    )
