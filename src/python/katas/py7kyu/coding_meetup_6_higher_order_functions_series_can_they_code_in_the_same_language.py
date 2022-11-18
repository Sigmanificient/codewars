"""Kata url: https://www.codewars.com/kata/58287977ef8d4451f90001a0."""


def is_same_language(lst):
    return all(
        p1['language'] == p2['language']
        for p1, p2 in zip(lst, lst[1::])
    )


def test_is_same_language():
    assert is_same_language(
        [
            {
                'firstName': 'Daniel',
                'lastName': 'J.',
                'country': 'Aruba',
                'continent': 'Americas',
                'age': 42,
                'language': 'JavaScript'
            },
            {
                'firstName': 'Kseniya',
                'lastName': 'T.',
                'country': 'Belarus',
                'continent': 'Europe',
                'age': 22,
                'language': 'JavaScript'
            },
            {
                'firstName': 'Hanna',
                'lastName': 'L.',
                'country': 'Hungary',
                'continent': 'Europe',
                'age': 65,
                'language': 'JavaScript'
            },
        ]
    )
    assert not is_same_language(
        [
            {
                'firstName': 'Mariami',
                'lastName': 'G.',
                'country': 'Georgia',
                'continent': 'Europe',
                'age': 29,
                'language': 'Python'
            },
            {
                'firstName': 'Mia',
                'lastName': 'H.',
                'country': 'Germany',
                'continent': 'Europe',
                'age': 39,
                'language': 'Ruby'
            },
            {
                'firstName': 'Maria',
                'lastName': 'I.',
                'country': 'Greece',
                'continent': 'Europe',
                'age': 32,
                'language': 'C'
            },
        ]
    )
