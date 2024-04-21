"""Kata url: https://www.codewars.com/kata/56f5594a575d7d3c0e000ea0."""


NO_CONF = 'No worthwhile conferences this year!'


def conference_picker(cities_visited, cities_offered):
    f = [o for o in cities_offered if o not in cities_visited]
    return f[0] if f else NO_CONF


def test_conference_picker():
    assert conference_picker(
        [], ['Philadelphia', 'Osaka', 'Tokyo', 'Melbourne']
    ) == 'Philadelphia'
    assert conference_picker(
        [], ['Brussels', 'Madrid', 'London']
    ) == 'Brussels'
    assert conference_picker(
        [], ['Sydney', 'Tokyo']
    ) == 'Sydney'
    assert conference_picker(
        [
            'London', 'Berlin', 'Mexico City',
            'Melbourne', 'Buenos Aires', 'Hong Kong', 'Madrid', 'Paris'
        ], ['Berlin', 'Melbourne']
    ) == NO_CONF
    assert conference_picker(
        [
            'Beijing', 'Johannesburg', 'Sydney',
            'Philadelphia', 'Hong Kong', 'Stockholm',
            'Chicago', 'Seoul', 'Mexico City', 'Berlin'
        ],
        ['Stockholm', 'Berlin', 'Chicago']
    ) == NO_CONF
    assert conference_picker(
        [
            'Mexico City', 'Dubai', 'Philadelphia', 'Madrid',
            'Houston', 'Chicago',  'Delhi', 'Seoul', 'Mumbai',
            'Lisbon', 'Hong Kong', 'Brisbane', 'Stockholm',
            'Tokyo', 'San Francisco', 'Rio De Janeiro'
        ],
        ['Lisbon', 'Mexico City']
    ) == NO_CONF