def is_digit(x: str) -> bool:
    """Kata url: https://www.codewars.com/kata/57126304cdbf63c6770012bd."""
    try:
        _ = float(x)
        return True

    except ValueError:
        return False
