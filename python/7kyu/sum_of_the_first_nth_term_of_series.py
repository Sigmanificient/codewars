def series_sum(n: int) -> str:
    """Kata url: https://www.codewars.com/kata/555eded1ad94b00403000071."""
    return f"{sum(1/(1 + 3 * x) for x in range(n)):.2f}"
