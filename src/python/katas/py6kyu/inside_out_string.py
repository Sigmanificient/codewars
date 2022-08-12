"""Kata url: https://www.codewars.com/kata/57ebdf1c2d45a0ecd7002cd5."""


def inside_out(st: str) -> str:
    out = []
    for word in st.split(' '):
        length = len(word)

        if length > 3:
            cut = length // 2

            middle = word[cut] if length % 2 else ''
            inside_out_word = word[:cut][::-1] + middle + word[-cut:][::-1]

        else:
            inside_out_word = word

        out.append(inside_out_word)

    return ' '.join(out)


def test_inside_out():
    assert inside_out(
        'man i need a taxi up to ubud'
    ) == 'man i ende a atix up to budu'

    assert inside_out(
        'what time are we climbing up the volcano'
    ) == 'hwta item are we milcgnib up the lovcona'

    assert inside_out('take me to semynak') == 'atek me to mesykan'
    assert inside_out(
        'massage yes massage yes massage'
    ) == 'samsega yes samsega yes samsega'
    assert inside_out(
        'take bintang and a dance please'
    ) == 'atek nibtgna and a adnec elpesa'
