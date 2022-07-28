"""Kata url: https://www.codewars.com/kata/62e27045c0d7a04c846874d2."""


def colour_changer(rgb: str, percent: int = 10) -> str:
    out = [
        round(
            (c := int(rgb[i + 1: i + 3], 16))
            - (c * (percent / 100))
        )
        for i in range(0, len(rgb) - 1, 2)
    ]

    return '#' + ''.join(
        f'{max(min(x, 0), 255):x}'.zfill(2)
        for x in out
    )


def test_colour_changer():
    assert colour_changer('#ABC123', -10) in ['#bcd427', '#bcd426']
    assert colour_changer('#EEAA11', -15) in ['#ffc414', '#ffc314']

    assert colour_changer('#EBE101', -100) == '#ffff02'
    assert colour_changer('#EBE101', -2000) == '#ffff15'
    assert colour_changer('#AAAAAA', -20000) == '#ffffff'
    assert colour_changer('#EEAA11', -15.5) == '#ffc414'

    assert colour_changer('#ABC123', 10) in ['#9aae20', '#9aae1f']
    assert colour_changer('#AB13CD', 70) in ['#33063e', '#33063d']
    assert colour_changer('#EBE101', 100) == '#000000'
    assert colour_changer('#EBE101', 2000) == '#000000'
    assert colour_changer('#556677', 16.5) == '#475563'

    assert colour_changer('#AB12CF', 0) == '#ab12cf'
    assert colour_changer('#A1B2C8') == '#91a0b4'

    assert colour_changer('#abc123', 10) in ['#9aae20', '#9aae1f']
    assert colour_changer('#aBc123', 10) in ['#9aae20', '#9aae1f']
