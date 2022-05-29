from typing import List, Any, Iterable, AnyStr

import pytest


def chunks(lst: AnyStr, n: int) -> Iterable[Any]:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def hexdump(data: bytes) -> str:
    hex_dump: List[str] = []
    for address, line in enumerate(chunks(data, 16)):
        hex_vals: List[str] = list(chunks(bytes.hex(line), 2))

        hex_dump.append(
            '{:08x}: {:47}  {}'.format(
                address * 16,
                ' '.join(hex_vals),
                ''.join(
                    chr(char)
                    if 32 <= (char := int(h, 16)) <= 126 else '.'
                    for h in hex_vals
                )
            )
        )

    return '\n'.join(hex_dump)


def dehex(text: str) -> bytes:
    return b''.join(bytes.fromhex(line[10:-16]) for line in text.split('\n'))


def test_chunks():
    assert not list(chunks(b'', 2))
    alp = 'abcdefghijklmnopqrstuvwxyz'

    assert list(chunks(alp, 3)) == ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']
    assert list(chunks(alp, 4)) == ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz']
    assert list(chunks(alp, 5)) == ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z']


def test_hex_dump():
    data = b'\x00' * 16
    dump = '00000000: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................'

    assert hexdump(data) == dump
    assert dehex(dump) == data

    data = b'CodeWars'
    dump = '00000000: 43 6f 64 65 57 61 72 73                          CodeWars'

    assert hexdump(data) == dump
    assert dehex(dump) == data

    data = (
        b'\x1d\xc4\x15\x25\x91\xe6\x09\x59\x04\x99\x15\x29\x0a\x45\x21\x29'
        b'\x26\x8e\x74\xa0\x1a\xbe\x75\x68\x06\xdd\x70\x33\xa4\x77\x7a\x5d'
        b'\xb1\xba\x22\xa7\xcf\xcc\xf7\xef\xb1\xe3\x13\xed\xf1\x89\xad\xad'
        b'\xb8\x2a\x52\x32\x65\x79\x43\x99\x6f\xc8\xd3\x8e\xb2\x5f\x50\xc9'
        b'\x08\x4a\x12\x25\x79\xc2\xdd\x31\x6b\xb8\x77\x74\x4b\x68\x4b\xd4'
        b'\xdb\x4e\x92\x09\xd5\x4c\x9f\x0b\xfd\xa9\xd1\xd6\x13\xf5\xf8\x81'
    )

    dump = (
        '00000000: 1d c4 15 25 91 e6 09 59 04 99 15 29 0a 45 21 29  ...%...Y...).E!)\n'
        '00000010: 26 8e 74 a0 1a be 75 68 06 dd 70 33 a4 77 7a 5d  &.t...uh..p3.wz]\n'
        '00000020: b1 ba 22 a7 cf cc f7 ef b1 e3 13 ed f1 89 ad ad  ..".............\n'
        '00000030: b8 2a 52 32 65 79 43 99 6f c8 d3 8e b2 5f 50 c9  .*R2eyC.o...._P.\n'
        '00000040: 08 4a 12 25 79 c2 dd 31 6b b8 77 74 4b 68 4b d4  .J.%y..1k.wtKhK.\n'
        '00000050: db 4e 92 09 d5 4c 9f 0b fd a9 d1 d6 13 f5 f8 81  .N...L..........'
    )

    assert hexdump(data) == dump
    assert dehex(dump) == data
