"""Kata url: https://www.codewars.com/kata/586538146b56991861000293."""
from typing import Dict

NATO: Dict[str, str] = {
    w[0].upper(): w for w in (
        'Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf',
        'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November',
        'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform',
        'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu'
    )
}


def to_nato(words: str) -> str:
    return ' '.join(
        NATO.get(word.upper(), word)
        for word in words
        if word != ' '
    )


def test_to_nato():
    assert to_nato('.d?d!') == '. Delta ? Delta !'

    assert to_nato('If you can read') == (
        "India Foxtrot Yankee Oscar Uniform "
        "Charlie Alfa November Romeo Echo Alfa Delta"
    )
    assert to_nato('Did not see that coming') == (
        "Delta India Delta November Oscar Tango Sierra "
        "Echo Echo Tango Hotel Alfa Tango Charlie Oscar "
        "Mike India November Golf"
    )
