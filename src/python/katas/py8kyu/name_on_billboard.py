"""Kata url: https://www.codewars.com/kata/570e8ec4127ad143660001fd."""


def billboard(name, price=30):
    return len(name) / (1 / price)


def test_billboard():
    assert billboard("Jeong-Ho Aristotelis") == 600
    assert billboard("Abishai Charalampos") == 570
    assert billboard("Idwal Augustin") == 420
    assert billboard("Hadufuns John", 20) == 260
    assert billboard("Zoroaster Donnchadh") == 570
    assert billboard("Claude Miljenko") == 450
    assert billboard("Werner Vigi", 15) == 165
    assert billboard("Anani Fridumar") == 420
    assert billboard("Paolo Oli") == 270
    assert billboard("Hjalmar Liupold", 40) == 600
    assert billboard("Simon Eadwulf") == 390
