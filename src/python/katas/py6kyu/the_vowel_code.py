ENCODE = str.maketrans("aeiou", "12345")
DECODE = str.maketrans("12345", "aeiou")


def encode(st: str) -> str:
    return st.translate(ENCODE)


def decode(st: str) -> str:
    return st.translate(DECODE)


def test_code():
    assert encode("hello") == "h2ll4"
    assert encode("How are you today?") == "H4w 1r2 y45 t4d1y?"
    assert encode("This is an encoding test.") == "Th3s 3s 1n 2nc4d3ng t2st."
    assert decode("h2ll4") == "hello"
