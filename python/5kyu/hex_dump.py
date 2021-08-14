from typing import List, Any, Iterable, Sized


def chunks(lst: Sized, n: int) -> Iterable[Any]:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def hexdump(data: bytes) -> str:
    hex_dump: List[str] = []
    for address, line in enumerate(chunks(data, 16)):
        hex_vals: List[str] = list(chunks(bytes.hex(line), 2))

        hex_dump.append(
            '{:0x} {:47}  {}'.format(
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
