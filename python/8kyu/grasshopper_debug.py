def weather_info(temp: float) -> str:
    """Kata url: https://www.codewars.com/kata/55cb854deb36f11f130000e1."""
    c = convert_to_celsius(temp)
    return f"{c} is {'above ' * (c > 0)}freezing temperature"


def convert_to_celsius(temperature: float) -> float:
    return (temperature - 32) * (5 / 9)
