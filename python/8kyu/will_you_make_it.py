def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    """Kata url: https://www.codewars.com/kata/5861d28f124b35723e00005."""
    return distance_to_pump <= mpg * fuel_left
