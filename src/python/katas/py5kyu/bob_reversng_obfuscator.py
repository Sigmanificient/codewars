"""Kata url: https://www.codewars.com/kata/559ee79ab98119dd0100001d."""


def decoder(encoded: str, marker: str) -> str:
    sections = encoded.split(marker)
    return ''.join(sections[::2]) + ''.join(sections[1::2])[::-1]


def test_decoder():
    assert decoder(
        'q.tile gnicsipida rutetcesnoc ,tema tis rolod muspi meroL', 'q'
    ) == 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

    assert decoder(
        'Duq.ucra missingid eusirelecs ,a orebil di sittam ,merol anru si', 'q'
    ) == 'Duis urna lorem, mattis id libero a, scelerisue dignissim arcu.'

    assert decoder(
        'Proinq.tile sitrobol rotittrop ,'
        'non muspi siu dnefiele ,sutcel neipas ',
        'q'
    ) == 'Proin sapien lectus, eleifend uis ipsum non, porttitor lobortis elit.'

    assert decoder(
        'q.qSusqsitanenev cen lsin sillom subinif ecsuF .itnetop essidnep', 'q'
    ) == 'Suspendisse potenti. Fusce finibus mollis nisl nec venenatis.'

    assert decoder(
        'Dq.silucaiqonec mollq odommoc qis ipsum qlsin lev', 'q'
    ) == 'Donec mollis ipsum vel nisl commodo iaculis.'
