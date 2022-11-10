"""kata url: https://www.codewars.com/kata/57158fb92ad763bb180004e7."""


def rain_amount(mm):
    if mm < 40:
        return f"You need to give your plant {40 - mm}mm of water"
    else:
        return "Your plant has had more than enough water for today!"


def test_rain_amount():
    enough = "Your plant has had more than enough water for today!"
    assert rain_amount(100) == enough
    assert rain_amount(40) == enough
    assert rain_amount(39) == "You need to give your plant 1mm of water"
    assert rain_amount(5) == "You need to give your plant 35mm of water"
    assert rain_amount(0) == "You need to give your plant 40mm of water"
