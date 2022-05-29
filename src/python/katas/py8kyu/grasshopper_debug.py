"""Kata url: https://www.codewars.com/kata/55cb854deb36f11f130000e1."""


def weather_info(temp: float) -> str:
    c: float = convert_to_celsius(temp)
    return f"{c} is {'above ' * (c > 0)}freezing temperature"


def convert_to_celsius(temperature: float) -> float:
    return (temperature - 32) * (5 / 9)
