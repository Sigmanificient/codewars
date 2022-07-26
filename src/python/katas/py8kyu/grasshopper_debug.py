"""Kata url: https://www.codewars.com/kata/55cb854deb36f11f130000e1."""


def weather_info(temp: float) -> str:
    c: float = convert_to_celsius(temp)
    return f"{c} is {'above ' * (c > 0)}freezing temperature"


def convert_to_celsius(temperature: float) -> float:
    return (temperature - 32) * (5 / 9)


def test_weather_info():
    assert weather_info(50) == "10.0 is above freezing temperature"
    assert weather_info(23) == "-5.0 is freezing temperature"


def test_convert_to_celsius():
    assert convert_to_celsius(32) == 0
    assert convert_to_celsius(68) == 20

    assert round(convert_to_celsius(100), 3) == 37.778
    assert round(convert_to_celsius(0), 3) == -17.778
    assert round(convert_to_celsius(20), 3) == -6.667
    assert round(convert_to_celsius(30), 3) == -1.111
