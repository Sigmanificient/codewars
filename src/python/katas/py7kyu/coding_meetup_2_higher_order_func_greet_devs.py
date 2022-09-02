"""Kata url: https://www.codewars.com/kata/58279e13c983ca4a2a00002a."""


def greet_developers(lst):
    for people in lst:
        people['greeting'] = (
            f"Hi {people['firstName']}, "
            f"what do you like the most about {people['language']}?"
        )

    return lst


def test_greet():
    assert greet_developers(
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

    ) == [
        {
            'firstName': 'Sofia',
            'lastName': 'I.',
            'country': 'Argentina',
            'continent': 'Americas',
            'age': 35,
            'language': 'Java',
            'greeting': 'Hi Sofia, what do you like the most about Java?'
        },
        {
            'firstName': 'Lukas',
            'lastName': 'X.',
            'country': 'Croatia',
            'continent': 'Europe',
            'age': 35,
            'language': 'Python',
            'greeting': 'Hi Lukas, what do you like the most about Python?'
        },
        {
            'firstName': 'Madison',
            'lastName': 'U.',
            'country': 'United States',
            'continent': 'Americas',
            'age': 32,
            'language': 'Ruby',
            'greeting': 'Hi Madison, what do you like the most about Ruby?'
        }
    ]
